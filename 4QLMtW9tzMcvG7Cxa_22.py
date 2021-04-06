
def resistance_calculator(resistors):
  par = 0 if any(r == 0 for r in resistors) else round(1/sum(1/r for r in resistors),2)
  return [par,round(sum(resistors),2)]

