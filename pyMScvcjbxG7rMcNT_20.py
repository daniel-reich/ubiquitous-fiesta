
def sum_list(lst):
    i = 0
    for x in lst:
        if type(x) == int:
            i += x
        else:
            i += sum_list(x)
    return i

