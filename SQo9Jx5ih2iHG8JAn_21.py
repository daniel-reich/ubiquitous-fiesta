
def expanded_form(n):
    lst=[]
    
    for i in range(len(list(str(n)))):
        lst.append(list(str(n))[i]+'0'*(len(list(str(n)))-i-1))
    for x in lst:
        if list(x)[0]=='0':
            lst.remove(x)
    for x in lst:
        if list(x)[0]=='0':
            lst.remove(x)
    
    return ' + '.join(lst)

