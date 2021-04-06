
def tuck_in(lst1, lst2):
    for n in lst2:
        lst1.append(n)
    lst1.append(lst1[1])
    lst1.pop(1)
    return(lst1)

