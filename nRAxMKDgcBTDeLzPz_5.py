
def circular_shift(lst1, lst2, n):
    lst2 = lst2[n:]+lst2[:n]
    if lst2==lst1:
        return True
    else:
        return False

