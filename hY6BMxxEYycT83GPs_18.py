
def multiply_by_11(n):
    myans = n[-1]
    c = 0
    for i in range(len(n)-1,0,-1):
        myans = chr((ord(n[i])-48 + ord(n[i-1])-48 + c)%10 + 48) + myans        
        if ord(n[i])-48 + ord(n[i-1])-48 + c > 9:
            c = 1
        else:
            c = 0
    myans = chr((ord(n[0])-48 + c)%10+48) + myans
    if n[0] == '9' and c == 1:
        myans = '1' + myans 
    
    return myans

