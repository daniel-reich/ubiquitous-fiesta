
def straight_digital(number):
  x = str(number)
  if number < 100: return 'Not Straight'
  elif len(set(x))==1: return 'Trivial Straight'
  for i in range(1, len(x)-1):
    if int(x[i]) - int(x[i-1]) != int(x[i+1]) - int(x[i]):
      return 'Not Straight'
  return int(x[i]) - int(x[i-1])

