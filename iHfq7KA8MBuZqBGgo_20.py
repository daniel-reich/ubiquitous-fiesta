
def is_legitimate(lst):
    return 1 not in lst[0] + lst[-1] + [i[0] for i in lst] + [i[-1] for i in lst]

