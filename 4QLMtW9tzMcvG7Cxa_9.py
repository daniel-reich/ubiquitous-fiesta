
def resistance_calculator(resistors):
  try:
    p = [1/i for i in resistors]
    parallel = round(1/sum(p),2)
  except:
    parallel = 0
  return [parallel, round(sum(resistors),2)]

