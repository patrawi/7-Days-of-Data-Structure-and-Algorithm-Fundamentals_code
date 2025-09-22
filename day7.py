def maxSubarray(arr):
   memo = {}
   memo_one_del = {}
   def solve_one_del(arr, i):
           if len(arr) == 0: return 0
           if i < 0: return -float('inf')
           if i == 0: return -float('inf')

           if i in memo_one_del: return memo_one_del[i]

           a_1 = solve_no_del(arr, i - 1)

           a_2 = solve_one_del(arr,i - 1) + arr[i]
           better_a = max(a_1, a_2)
           # b = arr[i] This line is for starting a brand new test so we don't do this in solve_one_del
           memo_one_del[i] = better_a
           return memo_one_del[i]
   def solve_no_del(arr, i):
       if len(arr) == 0: return 0
       if i == 0: return arr[0]
       if i < 0: return -float('inf')

       # recursive case
       if i in memo: return memo[i]
       a = solve_no_del(arr, i - 1) + arr[i]
       b = arr[i]
       memo[i] = max(a, b)
       return memo[i]




   solve_no_del(arr, len(arr) - 1)
   solve_one_del(arr,len(arr)-1)
   # Find max value in memo
   answer = arr[0] # Initialize with first element
   for key in memo:
       answer = max(answer, memo[key])
   for key in memo_one_del:
       answer = max(answer, memo_one_del[key])
   print(memo)

   return answer

print(maxSubarray([1, -2, 3, 10, -4, 7, 2, -5]))
print(maxSubarray([1, -2, 0, 3]))
print(maxSubarray(( [-10, 2, 3, 4])))
