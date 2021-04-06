
def last_name_lensort(lst):
    lst=[(x.split(' ')) for x in lst]
    lst = sorted(lst, key=lambda x: (len(x[1]), x[1]))
    return [" ".join(x) for x in lst]

