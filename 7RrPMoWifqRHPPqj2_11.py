
def highOrLow(x):
  if x > 99:
    x = x - 100
    return x
  elif x < 0:
    x = x + 100
    return x
  else:
    return x
  
def safecracker(start, increments):
  a = increments[0]
  b = increments[1]
  c = increments[2]
​
  aa = start - a
  aa = highOrLow(aa)
  bb = aa + b
  bb = highOrLow(bb)
  cc = bb - c
  cc = highOrLow(cc)
  return [aa, bb, cc]

