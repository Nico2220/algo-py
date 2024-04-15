
def sortArray(arr, n):
    zeros = 0
    ones = 0
    twos = 0

    for i in range(n):
        if arr[i] == 0:
            zeros += 1
        elif arr[i] == 1:
            ones +=1
        else :
            twos +=1
    print(twos)
    
    k = 0
    for i in range(zeros):
        arr[k] = 0
        k += 1
    for i in range(ones):
        arr[k] = 1
        k += 1
    for i in range(twos):
        arr[k] = 2
        k += 1
    return arr

print(sortArray([2, 2, 2, 2, 0, 0, 1, 0], 8))