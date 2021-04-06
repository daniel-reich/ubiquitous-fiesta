
def tuck_in(lst1, lst2):
    for x,y in enumerate(lst2):
         lst1.insert(x+1, y)
    return lst1

