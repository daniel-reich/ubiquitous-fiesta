
def transpose(lst):
    return list(zip(*lst))[::-1]
​
def spiral_transposition(lst):
    lst2 = []
    while lst:
        lst2 += lst.pop(0)
        lst = transpose(lst)
    return lst2

