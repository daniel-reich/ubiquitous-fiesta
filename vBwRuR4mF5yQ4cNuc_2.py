
def sum_of_missing_nums(lst):
    lst = sorted([int(c) for c in lst if c.isnumeric()])
    return lst[-1] - lst[0] - len(lst) + 1

