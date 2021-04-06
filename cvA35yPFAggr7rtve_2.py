
def last_ancestor(folders, X, Y):
    parent = {}
    for x, lst in folders.items():
        parent.update((y,x) for y in lst)
    sx, sy = set(X), set(Y)
    while not sx & sy:
        X = parent.get(X, X)
        Y = parent.get(Y, Y)
        sx.add(X)
        sy.add(Y)
    return (sx & sy).pop()

