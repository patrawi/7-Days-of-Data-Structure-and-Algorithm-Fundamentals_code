from multiprocessing.dummy import Array
def reverse(str):

    last_char = ''
    if len(str) != 0:
       last_char = str[-1]
    else :
        return ''
    return last_char + reverse(str[:-1])

def flatten(arr):
    # arr =  [1, [2], [[3], 4], [[[[5]]]]]
    # result = [1,2,3,4,5]
    # จะคืนค่า “array of numbers ที่มีตัวเลขทั้งหมดที่อยู่ใน arr อยู่ในนั้น”
    new_data = []

    for e in arr:
        if  isinstance(e, list):
             new_data.extend(flatten(e))
        else:
            new_data.append(e)
    return new_data

















def main():
    str = "learnalgorithm"
    set_list = [1, [2], [[3], 4], [[[[5]]]]]
    #print(reverse(str))
    print(flatten(set_list))


if __name__ == "__main__":
    main()
