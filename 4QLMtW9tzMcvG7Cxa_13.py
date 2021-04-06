
def resistance_calculator(resistors):
    parallel = 0 if 0 in resistors else 1/sum(1/i for i in resistors)
    return [round(parallel, 2), round(sum(resistors), 2)]

