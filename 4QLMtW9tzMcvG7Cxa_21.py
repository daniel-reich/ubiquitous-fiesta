
def resistance_calculator(resistors):
    return [round(1/(sum(list(map(lambda x:1/x,resistors)))), 2) if 0 not in resistors else 0,  round(sum(resistors), 2)]

