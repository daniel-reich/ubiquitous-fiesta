
def even_or_odd(s):
  odd = 0
  even = 0
  for i in s:
    if int(i) % 2 == 0:
      even += int(i)
    else:
      odd += int(i)
  if odd == even:
    return "Even and Odd are the same"
  elif odd > even:
    return "Odd is greater than Even"
  else:
    return "Even is greater than Odd"

