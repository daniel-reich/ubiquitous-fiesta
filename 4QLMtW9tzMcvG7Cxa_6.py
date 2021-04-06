
def resistance_calculator(resistors):
  try:
    return [round(1/sum([1/a for a in resistors]),2),round(sum(resistors),2)]
  except ZeroDivisionError:
    return [0,sum(resistors)]

