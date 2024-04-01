def rotateArray(arr, k):
    for i in range(0,k):
        temp = arr[0]
        for j in range(1, len(arr)):
            arr[j-1] = arr[j]
        arr[len(arr) - 1] = temp
    return arr