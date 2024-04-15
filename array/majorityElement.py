def majorityElement(v):
    pointerOne = 0
    pointerTwo = 0
    count = 0
    while pointerOne < len(v) and pointerTwo < len(v):
        if v[pointerOne] == v[pointerTwo]:
            count += 1
        else:
            count -= 1
        
        if count == 0:
            pointerOne = pointerTwo + 1

        pointerTwo += 1
    
    count2 = 0
    if count > 0 :
        for i in range(len(v)):
            if v[i] == v[pointerOne]:
                count2 += 1
            if count2 > len(v) // 2:
                return v[pointerOne]
    
    return -1

            
                

print(majorityElement([2, 2, 1, 3, 1, 1, 3, 1, 1]))