
def vertical_txt(txt):
    lst=txt.split(' ')
    max=0
    lst2=[]
    for i in lst:
        if len(i)>max:
            max=len(i)
    for i in lst:
        lst2.append(i+' '*(max-len(i)))
    result=[]
    for i in range(max):
        temp=[]
        for j in lst2:
            temp.append(j[i])
        result.append(temp)
    return result

