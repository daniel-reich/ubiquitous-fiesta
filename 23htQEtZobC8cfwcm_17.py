
def canConcatenate(lst, target):
    from itertools import chain
    return sorted(chain.from_iterable(lst)) == sorted(target)

