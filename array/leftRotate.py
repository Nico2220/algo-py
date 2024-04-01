def leftRotate(n, a):
    temp = a[0]
    for i in range(1, n):
        a[i - 1] = a[i]
    a[n-1] = temp
    return a