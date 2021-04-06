
def flatten(lst):
    if not lst:
        return []
    if type(lst[0]) == list:
        return flatten(lst[0]) + flatten(lst[1:])
    return lst[:1] + flatten(lst[1:])

