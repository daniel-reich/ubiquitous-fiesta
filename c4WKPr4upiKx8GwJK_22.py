
def duplicate_nums(l):
    return sorted(list(set([x for x in l if l.count(x) > 1]))) or None

