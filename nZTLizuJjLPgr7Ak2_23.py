
def additive_inverse(lst):
  nueva = []
  for x in lst:
    if x > 0: 
      nueva.append(x * -1)
    elif x < 0:
      nueva.append(abs(x))
  return nueva

