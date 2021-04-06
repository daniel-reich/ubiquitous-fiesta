
def is_anti_list(lst1, lst2):
    items = list(set(lst1))
    return [items[1] if s==items[0] else items[0] for s in lst1] == lst2

