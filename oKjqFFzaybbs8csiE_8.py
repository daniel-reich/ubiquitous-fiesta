
def cons(lst):
    minimum=min(lst)
    maximum=max(lst)
    new_lst=sorted(lst)
    l=[]
    for i in lst:
        if lst.count(i)>1:
            return False
    for i in range(minimum,maximum+1):
        l.append(i)
    if l==new_lst:
        return True
    else:
        return False

