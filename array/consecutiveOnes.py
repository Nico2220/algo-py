def consecutiveOnes(arr):
    longest = 0
    currCount = 0
    for i in range(0, len(arr)):
        if arr[i] == 1:
            currCount += 1
            if longest < currCount:
                longest = currCount
        else:  
            currCount = 0
    return longest

        

print(consecutiveOnes([1, 0,  1, 0, 1, 1, 1, 0]))