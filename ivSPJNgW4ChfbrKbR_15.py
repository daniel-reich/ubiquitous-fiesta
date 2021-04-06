
def soroban(frame):
    upper=''
    for i in frame[1]:
        if i=='O':
            upper+='5'
        else:
            upper+='0'            
    lower=''
    for i in range(7):
        k=0
        for j in range(3,8,1):
            if frame[j][i]=='|':
                break
            else:
                k+=1
        lower+=str(k)
    return int(upper)+int(lower)

