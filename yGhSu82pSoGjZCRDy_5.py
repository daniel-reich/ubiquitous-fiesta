
def seesaw(num):
  x = ''.join([i for i in str(num)[:int(len(str(num)) / 2)]])
  y = ''.join([i for i in str(num)[round(len(str(num)) / 2):]])
  if x == y or len(str(num)) == 1 or num == None:
    return 'balanced'
  elif x > y:
    return 'left'
  else:
    return 'right'

