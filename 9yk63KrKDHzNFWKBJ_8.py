
def is_it_inside(folders, X, Y):
​
    if X == Y or (Y in folders and (X in folders[Y] or any([is_it_inside(folders, X, a) for a in folders[Y]]))):
        return True
    return False

