
def last_ancestor(folders, X, Y):
    if X == Y:
        return X
    x = [X]
    y = [Y]
    while True:
        l = len(y)
        for key, value in folders.items():
            if y[-1] in value:
                y.append(key)
        if l == len(y):
            break
    while True:
        l = len(x)
        for key, value in folders.items():
            if x[-1] in value:
                x.append(key)
        if l == len(x):
            break
    for i in x:
        if i in y:
            return i

