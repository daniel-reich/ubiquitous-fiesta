
def maya_number(n):
    temp = []
    myans = []
    t = -1
    
    for i in range(10,-1,-1):
        temp.append(n//(20**i))
        n = n - n//(20**i)*20**i
    
    for i in range(len(temp)):
        if temp[i] != 0:
            t = i
            break
    if t == -1:
        return ['@']    
    
    for i in range(t,len(temp)):
        if temp[i] == 0:
            temp[i] = '@'
        else:
            a = temp[i]
            b = a // 5
            c = a - b*5
            temp[i] = 'o'*c + '-'*b        
    
    return temp[t:]

