
def sum_list(lst):
    if type(lst) == int:
        return lst
    if not lst:
        return 0
    return sum_list(lst[0]) + sum_list(lst[1:])

