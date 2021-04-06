
def sum_list(lst):
    if len(lst) == 0:
        return 0
    elif len(lst) == 1 and type(lst[0]) == int:
        return lst[0]
    elif type(lst[0]) == int:
        return lst[0] + sum_list(lst[1:])
    return sum_list(lst[0]) + sum_list(lst[1:])

