
def sock_merchant(lst):
    s = list(set(lst))
    res =[]
    for v in s:
        res.append(lst.count(v)//2)
    return sum(res)

