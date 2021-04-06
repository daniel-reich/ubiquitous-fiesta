
def plant_trees(w, l, g):
    if g != 0:
        if (2*w+2*(l-2)) % (g+1) == 0:
            return (2*w+2*(l-2)) // (g+1)
        else:
            return 0
    return 2*w+2*(l-2)

