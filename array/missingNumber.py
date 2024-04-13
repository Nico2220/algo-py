from typing import *

def missingNumber(a : List[int], N : int) -> int:
    xor1 = 0
    xor2 = 0
    for i in range(0, N-1):
        xor2 = xor2 ^ a[i]
        xor1 = xor1 ^ (i + 1)
    xor1 = xor1 ^ N
    return xor1 ^ xor2


print(missingNumber([1,2,4,5], 5))