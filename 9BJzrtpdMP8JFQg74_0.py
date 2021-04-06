
def twins(lst):
    return next(i for i in range(len(lst)) if sum(lst[:i]) == sum(lst[i:]))

