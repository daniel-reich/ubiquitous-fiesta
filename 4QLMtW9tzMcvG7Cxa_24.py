
def resistance_calculator(resistors):
  try:
    return [round(1/sum(1/i for i in resistors),2),round(sum(resistors),2)]
  except:
    return [0,round(sum(resistors),2)]

