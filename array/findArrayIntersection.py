def findArrayIntersection(arr: list, n: int, brr: list, m: int):
    pointerOne = 0
    pointerTwo = 0
    result = []
    while pointerOne < n and pointerTwo < m:
        if arr[pointerOne] < brr[pointerTwo]:
            pointerOne += 1
        elif arr[pointerOne] > brr[pointerTwo]:
            pointerTwo += 1
        else:
            result.append(arr[pointerOne])
            pointerOne += 1
            pointerTwo += 1

    return result

print(findArrayIntersection([1,2,2,2,3,4], 6, [2,2,3,3], 4))