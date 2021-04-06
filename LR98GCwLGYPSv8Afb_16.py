
def pluralize(lst):
    s = set(lst)
    return  {item+'s' if lst.count(item) >1 else item for item in s}

