
def pluralize(lst):
    last=[]
    lst1=set(lst)
    lst1=list(lst1)
    for i in lst1:
        if lst.count(i)==1:
            last.append(i)
        else:
            last.append(i+'s')
    return set(last)

