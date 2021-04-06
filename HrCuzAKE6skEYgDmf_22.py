
def pairs(lst):
    result = []
    while len(lst) != 0:
        if len(lst) >= 2:
            result.append([lst.pop(0), lst.pop()])
        elif len(lst) == 1:
            result.append([lst[0], lst.pop()])
    return result

