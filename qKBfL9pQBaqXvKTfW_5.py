
def sum_of_slices(lst):
    result = []
    mem = 0
    for i in lst:
        if i + mem < 100:
            mem += i
        elif i + mem > 100:
            result += [mem]
            mem = i
        elif i + mem == 100:
            result += [mem+i]
            mem = 0
    if mem != 0:
        result += [mem]
    return result

