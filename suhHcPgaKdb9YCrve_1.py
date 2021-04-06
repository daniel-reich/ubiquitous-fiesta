
def even_or_odd(s):
  odd = 0
  even = 0
  for c in s:
    if int(c) % 2 == 0:
      even += int(c)
    else:
      odd += int(c)
  if even > odd:
    return 'Even is greater than Odd'
  elif even < odd:
    return 'Odd is greater than Even'
  return 'Even and Odd are the same'

