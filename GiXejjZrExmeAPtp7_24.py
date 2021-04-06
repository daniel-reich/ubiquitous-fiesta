
def fifth(*args):
    lst = []
    for x in args:
        lst.append(x)
    return type(lst[4]) if len(lst) >= 5 else "Not enough arguments"

