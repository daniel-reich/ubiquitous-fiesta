
def sort_authors(lst):
    lst2 = [(i.split()[-1][0]) for i in lst ]
    lst3 = sorted([(i[0].lower(),j) for j,i in enumerate(lst2)])
    return [lst[i[1]] for i in lst3]

