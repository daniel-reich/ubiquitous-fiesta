
def resistance_calculator(resistors):
  return [round(0 if 0 in resistors else 1 / sum(1/r for r in resistors), 2), round(sum(resistors), 2)]

