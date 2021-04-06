
def resistance_calculator(resistors):
  try:
    return [round(1/sum(list(map(lambda x: 1/x,resistors))),2), round(sum(resistors),2)]
  except ZeroDivisionError:
    return [0,sum(resistors)]

