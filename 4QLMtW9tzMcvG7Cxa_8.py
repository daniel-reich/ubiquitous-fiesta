
def resistance_calculator(resistors):
    try:
        return [round(1 / sum([1 / x for x in resistors]), 2), round(sum(x for x in resistors), 2)]
    except ZeroDivisionError:
        return [0, round(sum(x for x in resistors), 2)]

