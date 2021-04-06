
def not_share(lst1, lst2):
    return all([not i in lst2 for i in lst1])

