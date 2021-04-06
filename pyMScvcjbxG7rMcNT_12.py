
def sum_list(lst):
    if len(lst) == 0:
        return 0
    x = lst.pop()
    if type(x) == list:
        x = sum_list(x)
    return sum_list(lst)+x

