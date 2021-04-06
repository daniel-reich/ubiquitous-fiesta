
def sorting(s):
    lst=[]
    lst2=[]
    for i in s:
        if i.islower():
            lst.append(i)
        elif i.isupper():
            lst.append(i)
    lst.sort(key=lambda x:[ord(x.lower()),121-ord(x)])
    for i in s:
        if i.isdigit():
            lst2.append(i)
    lst2.sort()
    return ''.join(lst)+''.join(lst2)

