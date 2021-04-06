
def canConcatenate(lst, target):
    flat = lambda l: [i for sub in l for i in sub]
    return sorted(flat(lst)) == sorted(target)

