
def is_wristband(lst):
    
    horizontal = list(dict.fromkeys([len(list(dict.fromkeys(i))) for i in lst]))#horizontal
    vertical = list(dict.fromkeys([len(list(dict.fromkeys(i))) for i in [[j[i] for j in lst] for i in range(len(lst[0]))]])) #vertical
    leftright = list(dict.fromkeys([len(list(dict.fromkeys(i))) for i in [[c for c in r if c is not None] for r in zip(*[([None] * (len(lst) - 1))[i:] + r + ([None] * (len(lst) - 1))[:i] for i, r in enumerate(lst)])]]))
    rightleft = list(dict.fromkeys([len(list(dict.fromkeys(i))) for i in [[c for c in r if c is not None] for r in zip(*[([None] * (len(lst) - 1))[:i] + r + ([None] * (len(lst) - 1))[i:] for i, r in enumerate(lst)])]]))
​
    return True if [1] in [horizontal, vertical, leftright, rightleft] else False

