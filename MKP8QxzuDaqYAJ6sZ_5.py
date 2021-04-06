
def is_correct_aliases(names, aliases):
    x=['t' if i.split()[0][0]==i.split()[1][0] else 'f' for i in aliases]
    return False if 'f' in x else True

