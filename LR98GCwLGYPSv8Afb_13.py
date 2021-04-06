
def pluralize(l):
    return set([a + 's' if l.count(a) > 1 else a for a in l])

