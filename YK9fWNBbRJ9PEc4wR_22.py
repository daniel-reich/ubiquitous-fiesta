
def tuck_in(lst1, lst2):
    for n in range(len(lst1)):
        if n==0:
            lst2.insert(0,lst1[n])
        else:
            lst2.append(lst1[n])
    return lst2

