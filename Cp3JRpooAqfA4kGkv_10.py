
def node_type(lon, lop, n):
    if n not in lon:        return 'Not exist'
    if n not in lop:        return 'Leaf'
    i = lon.index(n)
    if lop[i] in lon:
        return 'Inner'
    return 'Root'

