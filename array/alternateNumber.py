def alternateNumbers(a):
    pos = 0
    neg = 1
    result = [0] * len(a)
    for i in range(len(a)):
        if a[i] < 0:
            result[neg] = a[i]
            neg +=2
        else:
            result[pos] = a[i]
            pos +=2
    return result
        

print(alternateNumbers([1, 2, -4, -5]))