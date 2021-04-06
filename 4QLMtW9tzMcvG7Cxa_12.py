
def resistance_calculator(resist):
  return ([round(1 / sum(1 / r for r in resist), 2), 
    round(sum(resist), 2)] if resist[1] else [0, resist[0]])

