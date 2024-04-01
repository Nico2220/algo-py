def largestNumber(array):
    largest = float('-inf')
    for i in range(0,len(array)):
        if array[i] > largest:
            largest = array[i]
    return largest
    
print(largestNumber([3,1,6,2,6,4]))