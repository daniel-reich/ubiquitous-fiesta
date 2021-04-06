
def not_share(lst1, lst2):
    for i in lst1:
        if i in lst2:
            return False
    return True

