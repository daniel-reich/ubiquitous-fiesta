
def simple_comp(lst1, lst2):
    if lst1 is None or lst2 is None or len(lst1) != len(lst2):
        return False
    lst1.sort(key=abs)
    lst2.sort()
    for i in range(len(lst1)):
        if lst1[i] ** 2 != lst2[i]:
            return False
    return True

