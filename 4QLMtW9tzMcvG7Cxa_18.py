
def resistance_calculator(resistors):
    s = sum(resistors)
    if s == 0:
        return [0, 0]
    return [0, s] if 0 in resistors else [round(1. / sum([1. / r for r in resistors]),2), round(s, 2)]

