
def tuck_in(lst1, lst2):
    mid = len(lst1) // 2
    return lst1[:mid] + lst2 + lst1[mid:]

