
def simple_comp(lst1, lst2):
    try:
        return sorted(lst2) == sorted(i**2 for i in lst1)
    except:
        return False

