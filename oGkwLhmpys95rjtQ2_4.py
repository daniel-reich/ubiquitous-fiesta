
def match_last_item(lst):
    new = []
    for el in lst:
        new.append(str(el))
    checker = new[-1]
    new.pop(-1)
    z = "".join(new)
    return checker == z

