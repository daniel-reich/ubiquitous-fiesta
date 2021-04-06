
def plant_trees(w, l, g):
    if w == 0 or l == 0:
        p = 0
    elif w == 1 or l == 1:
        p = w * l
    else: 
        p = (w * l) - (w - 2) * (l - 2) 
    if p % (g + 1) > 0:
        return 0
    else:
        return p // (g + 1)

