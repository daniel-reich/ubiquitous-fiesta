
def split(x):
  highest = 0
  for i in range(1, x+1):
    high = (x/i)**i
    if high > highest: highest = round(high,1)
  return highest

