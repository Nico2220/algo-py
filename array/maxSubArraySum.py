def maxSubarraySum(arr, n) :
    sum = float("-inf")
    currSum = 0
    for i in range(n):
        currSum += arr[i]

        if currSum > sum :
             sum = currSum
        
        if currSum < 0:
            currSum = 0
            
    if sum < 0:
        sum = 0
    return sum


# print(maxSubarraySum([1, 2, 7, -4, 3, 2, -10, 9, 1], 9))



