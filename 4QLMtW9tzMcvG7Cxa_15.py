
def resistance_calculator(resistors):
  if 0 in resistors: return [0, sum(resistors)]
  return [round(1/sum(1/i for i in resistors),2), round(sum(resistors),2)]

