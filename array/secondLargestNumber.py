def removeDuplicates(arr,n):
    i = 0
    for j in range(1, n):
        if arr[i]== arr[j]:
            continue
        else:
            arr[i + 1] = arr[j]
            i = i+1
    return i + 1