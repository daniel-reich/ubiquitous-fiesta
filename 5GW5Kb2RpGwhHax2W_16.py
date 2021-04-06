
def rotated(lst):
    return list(map(list, zip(*lst)))[::-1]
​
def spiral_transposition(lst):
    return lst and lst[0] + spiral_transposition(rotated(lst[1:]))

