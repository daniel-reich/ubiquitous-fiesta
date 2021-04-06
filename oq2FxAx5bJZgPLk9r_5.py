
def sock_merchant(lst):
    g = []
    for x in set(lst):
        g.append(lst.count(x) // 2)
    return(sum(g))

