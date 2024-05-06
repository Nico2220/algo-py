from typing import *

def nextGreaterPermutation(A : List[int]) -> List[int]:
    index = -1
    for i in range(len(A) - 2, -1, -1):
        if A[i] < A[i + 1]:
            index = i
            break
    
    if index == -1:
        A.reverse()
        return A
    


    for i in range(len(A) - 1, index, -1):
        if A[i] > A[index]:
            swap(i, index, A)
            break
    

    subA = list(reversed(A[index + 1:]))
    result = A[:index + 1] + subA
    return result
        
   


def swap(i, j, array):
    [array[i], array[j]] = [array[j], array[i]]


print(nextGreaterPermutation([1,3,2]))