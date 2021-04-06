
def shift_sentence(txt):
    lst=[]
    temp=""
    result=""
    for i in range(0,len(txt)):
        if(txt[i]!=' '):
            temp+=txt[i]
        else:
            lst.append(temp)
            temp=""
    lst.append(temp)
    if(len(lst)==1):
        return lst[0]
    else:
        for i in range(0,len(lst)):
            temp2=""
            for k in range(0,len(lst[i])):
                if(i==0):
                    if(k==0):
                        temp2+=lst[len(lst)-1][0]
                    else:
                        temp2+=lst[i][k]
                else:
                    if(k==0):
                        temp2+=lst[i-1][0]
                    else:
                        temp2+=lst[i][k]
            result+=temp2+" "
    return result[:len(result)-1]

