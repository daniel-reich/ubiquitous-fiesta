
import functools
def flatten(r):
    items = (flatten(i) if type(i) is list else [i] for i in r)
    return functools.reduce(list.__add__, items)

