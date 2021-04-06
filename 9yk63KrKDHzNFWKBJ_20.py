
def is_it_inside_rec(folders, target, parent, found):
    if parent in folders:
        if target in folders[parent]:
            found = True
        else:
            for child in folders[parent]:
                found = is_it_inside_rec(folders, target, child, found)
    return found
​
​
def is_it_inside(folders, X, Y):
    if X == Y:
        return True
    else:
        return is_it_inside_rec(folders, X, Y, found=False)

