
def super_digit(n, k):
    i = 0
    j = 0
    p = ''
    supernum = 0
    #concatanate value
    while i < k:
        p += n
        i +=1
    
    while int(p) >= 10:
        supernum = 0
        for j in range(len(p)):
            supernum += int(p[j])
        p = str(supernum)
​
    return(int(p))

