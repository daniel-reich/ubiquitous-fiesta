
def even_or_odd(s):
  e = 0
  o = 0
  for i in s:
    i = int(i)
    if i%2==0:
      e += i
    else:
      o += i
  if e > o:
    return "Even is greater than Odd"
  if o > e:
    return "Odd is greater than Even"
  return "Even and Odd are the same"

