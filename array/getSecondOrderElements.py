def getSecondOrderElements(n, a):
    secondLargest = getSecondSmallest(n, a)
    secondSmallest = getSecondLargest(n, a)
    return [secondLargest, secondSmallest]


def getSecondSmallest(n, a):
    l = float("-inf")
    sl = float("-inf")

    for i in range(0, n):
        if a[i] > l:
            sl = l
            l = a[i]
        elif a[i] < l and a[i] > sl:
            sl = a[i]
    return sl

def getSecondLargest(n, a):
    sm = float("inf")
    ssm = float("inf")
    for i in range(0, n):
        if a[i] < sm:
            ssm = sm
            sm = a[i]
        elif a[i] != sm and a[i] < ssm:
            ssm = a[i]
    return ssm



print(getSecondOrderElements(5, [1,2,5,3,1,4]))