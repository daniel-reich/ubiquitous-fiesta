
def add_it_up(lst):
    if isinstance(lst[0], int) or isinstance(lst[0], float):
        return sum(lst)
    elif isinstance(lst[0], list):
        return sum(lst, [])
    else:
        return sum(lst, ())

