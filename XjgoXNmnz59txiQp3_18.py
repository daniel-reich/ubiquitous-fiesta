
def split(number):
  x = number
  twos = 0
  threes = 0
  fours = 0
  while x > 1:
    if x > 4 or x==3:
      x = x-3
      threes = threes + 1
    elif x == 4:
      x = x-4
      fours = fours + 1
    elif x == 2: 
      x = x-2
      twos = twos + 1
  return (2**twos)*(3**threes)*(4**fours)

