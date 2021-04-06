
def resistance_calculator(resistors):
  series = round(sum(resistors), 2)
  
  if any(not r for r in resistors):
    parallel = 0
  else:
    parallel = round(1/sum(1/r for r in resistors), 2)
    
  return [parallel, series]

