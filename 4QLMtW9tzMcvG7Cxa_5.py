
def resistance_calculator(resistors):
  i = 0
  j = 0
  zero = False
  for x in resistors:
    if x != 0:
      i += x
      j += 1/x
    else:
      zero = True
  if zero:
    j = 0
  else: 
    j = 1/j
  return [round(j,2),round(i,2)]

