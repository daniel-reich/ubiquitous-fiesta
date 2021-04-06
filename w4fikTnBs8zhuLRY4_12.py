
def rep_set(n):
    lst = [[], [[]]]
    if n==0:
        return []
    if n==1:
        return [[]]
    for i in range(2,n):
        lst.append(lst[0:])
    return lst

