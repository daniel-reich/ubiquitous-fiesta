
def in_box(lst):
    return any([('*' in i and i.index('*') not in [0,len(i)]) for i in lst])

