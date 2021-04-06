
def count_datatypes(*args):
    lst = [type(i) for i in args]
    return [lst.count(i) for i in (int, str, bool, list, tuple, dict)]

