
def is_it_inside(folders, X, Y):
    if X == Y:
        return True
    y = []
    if Y in folders:
        y.append(Y)
    while True:
        if len(y) == 0:
            return False
        for i in y:
            if X in folders[i]:
                return True
            else:
                y.remove(i)
                for elem in folders[i]:
                    if elem in folders:
                        y.append(elem)

