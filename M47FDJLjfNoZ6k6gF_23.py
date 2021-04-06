
def cup_swapping(swaps):
  ball = 'B'
  for i in swaps:
    if (i == 'AB' or i == 'BA') and ball == 'B':
      ball = 'A'
    elif (i == 'AB' or i == 'BA') and ball == 'A':
      ball = 'B'
    elif (i == 'BC' or i == 'CB') and ball == 'B':
      ball = 'C'
    elif (i == 'BC' or i == 'CB') and ball == 'C':
      ball = 'B'
    elif (i == 'AC' or i == 'CA') and ball == 'A':
      ball = 'C'
    elif (i == 'AC' or i == 'CA') and ball == 'C':
      ball = 'A'
  return ball

