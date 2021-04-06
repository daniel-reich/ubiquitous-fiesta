
def get_length(lst):
    if len(lst)<1:
        return 0
    x = lst.pop(0)
    if isinstance(x, int):
        return 1+ get_length(lst)
    else:
        return get_length(x) + get_length(lst)

