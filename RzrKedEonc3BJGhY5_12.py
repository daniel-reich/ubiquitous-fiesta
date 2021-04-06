
def plant_trees(w, l, g):
    perimeter = 2*w + 2*l - 4
    if w == 0 or l == 0:
        return 0
    elif perimeter%(g+1) == 0:
        return int(perimeter/(g+1))
    else:
        return 0

