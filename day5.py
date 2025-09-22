from collections import deque
import math
def simulate(n, shortcuts, timeLimit):
    print(n)
    # Implement graph first
    G = {}
    V = n

    min_time = [math.inf] * (n+1)

    for i in range(V+1):
        G[i] = []

    for i in range(n):
        G[i].append(i+1)
    for u,v in shortcuts:
        G[u].append(v)

    queue = deque()
    min_time[0] = 0

    farthest_step = 0
    queue.append(0)
    while queue:
        s = queue.popleft()


        for neightbour in G[s]:

            if min_time[neightbour] == math.inf:
                min_time[neightbour] = min_time[s] + 1

                queue.append(neightbour)

    print(min_time)
    if min_time[n] <= timeLimit:
        return f"OK:{min_time[n]}"
    for i in range(len(min_time)):
        if min_time[i] == timeLimit:
            if i > farthest_step :
                farthest_step = i
    return f'ERR:{farthest_step}'

def main():
   print(simulate(8, [[0,3], [0,4], [3,7]], 100))
   print('----------\n')
   print(simulate(4, [[0,3]], 100))
   print('----------\n')
   print(simulate(8, [[0,3], [0,4], [3,7]], 1))
   print('----------\n')
   print(simulate(63, [[4,48],[19,29],[0,7]], 68))
   print(simulate(96,[[41,45],[15,34],[23,84],[66,86],[47,81],[93,95],[73,90],[85,86],[23,52],[31,89],[12,86],[38,44],[53,66],[17,54],[12,43],[69,89],[49,70]] , 20))



if __name__ == "__main__":
    main()
