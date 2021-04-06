
def resistance_calculator(resistors):
  return [round(1/sum(1/r for r in resistors),2) if all(resistors) else 0, 
          round(sum(resistors),2)]

