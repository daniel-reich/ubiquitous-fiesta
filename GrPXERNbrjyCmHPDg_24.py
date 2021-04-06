
def duplicate_count(txt):
    lst=[]
    lst2=[]
    for i in range(len(txt)):
        lst.append(txt[i])
        if lst.count(lst[i])>1:
            lst2.append(lst[i])
    return len(set(lst2))

