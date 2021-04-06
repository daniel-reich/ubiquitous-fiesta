
def operation(num1, num2):
  dd = {(num1+num2): 'added', (num1-num2): 'subtracted', (num1*num2): 'multiplied', (num1/num2): 'divided'}
  if 24 in dd.keys():
    return dd[24]
  else:
    return None

