
def resistance_calculator(resistors):
  par = 0 if 0 in resistors else sum([1/i for i in resistors])**-1
  ser = sum([i for i in resistors])
  return [round(par,2), round(ser,1)]

