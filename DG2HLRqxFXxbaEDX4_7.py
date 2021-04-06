
def return_only_integer(lst):
    return [x for x in lst if isinstance(x, int) and not isinstance(x, bool)]

