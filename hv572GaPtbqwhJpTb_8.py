
def elasticize(word):
    myans = ''
    a = 0
    if len(word) % 2 == 0:
        l = len(word)//2
    
        for i in range(1,l):
            myans += word[a]*i
            a += 1
        for i in range(l,l+1):
            myans += word[a]*i
            a += 1
        for i in range(l,l+1):
            myans += word[a]*i
            a += 1
        for i in range(l-1,0,-1):
            myans += word[a]*i
            a += 1  
    else:
        a = 0
        l = len(word)//2+1
        for i in range(1,l):
            myans += word[a]*i
            a += 1
        for i in range(l,l+1):
            myans += word[a]*i
            a += 1
        for i in range(l-1,0,-1):
            myans += word[a]*i
            a += 1
    
    return myans

