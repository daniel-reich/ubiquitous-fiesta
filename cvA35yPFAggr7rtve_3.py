
def last_ancestor(folders, X, Y):
    parents = {u:k for k,v in folders.items() for u in v}
    u = [v for v in parents.values() if v not in parents.keys()][0]
    parents[u] = "#"
    print(parents)
    while X in parents.keys():
        y = Y
        while y in parents.keys():
            if parents[y] == X or y == X:
                return X
            y = parents[y]
        X = parents[X]

