
def resistance_calculator(resistors):
  r = sum(1/i for i in resistors if i!=0)
  o = round(1/r if r else 0,2)
  return [0 if o==sum(resistors) else o , round(sum(resistors),2)]

