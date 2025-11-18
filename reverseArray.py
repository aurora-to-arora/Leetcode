def reverseArray(arr):

    temp = []
    n = len(arr)
    for i in range(n):
        temp.append(arr[n -i-1])
    arr=temp
    return arr
