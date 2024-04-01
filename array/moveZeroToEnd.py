def moveZeroToEnd(n, a):
    j = float("inf")
    for i in range(0, n):
        if a[i] == 0 :
            j = i
    
    if j== -1:
        return a
   
    for i in range(j+1, n):
        if a[i] != 0:
            swap(i, j, a)
            j +=1
    return a

def swap(i, j, a):
    temp = a[j]
    a[j] = a[i]
    a[i] = temp