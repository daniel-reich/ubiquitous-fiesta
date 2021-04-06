
def func(lst):
    return len(lst) + sum(func(x) for x in lst if type(x) == list) if lst else 0

