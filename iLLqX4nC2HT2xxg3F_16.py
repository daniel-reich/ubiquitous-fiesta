
def deepest(lst) :
    level = 0
    while lst :
        level += 1
        lst = [x for l in lst if isinstance(l,list) for x in l]
​
    return level

