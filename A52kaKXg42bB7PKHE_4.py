
def num_then_char(lst):
    l = []
    for elem in lst:
        for e2 in elem:
            l.append(e2)
    l1 = sorted([x for x in l if type(x) == float or type(x) == int])
    l2 = sorted([x for x in l if type(x) == str])
    l3 = (l1+l2)[::-1]
    l_new = []
    
    for elem in lst:
        l_block = []
        for e2 in elem:
            l_block.append(l3.pop())
        l_new.append(l_block)
    return l_new

