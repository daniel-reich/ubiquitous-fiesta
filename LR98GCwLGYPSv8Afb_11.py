
def pluralize(lst):
    return set('{}s'.format(w) if lst.count(w) >= 2 else w for w in lst)

