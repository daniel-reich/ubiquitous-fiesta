
def plant_trees(w, l, g):
    perimeter = 2 * w + 2 * (l - 2)
    if not perimeter % (1 + g):
        trees = perimeter // (1 + g)
        if not trees % 2:
            return trees
    return 0

