
def resistance_calculator(resistors):
    s = sum(resistors)
    if 0 in resistors:
        return [0, s]
    p = 1 / sum([1/x for x in resistors])
    return [round(p,2), round(s,2)]

