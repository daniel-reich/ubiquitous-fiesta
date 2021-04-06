
def last_name_lensort(names):
    return sorted(names, key=lambda x: (len(x[x.index(' ')+1:]), x[x.index(' '):]))

