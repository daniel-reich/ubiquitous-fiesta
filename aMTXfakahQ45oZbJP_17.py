
def complete_bracelet(lst):
    if len(lst)%2==1:return False
    l,l2 = [],[]
    for i in range(len(lst)):
        l.append(lst[i])
        if list(l)==lst[i+1:i+len(l)+1] and len(l)>1:return True
    return False

