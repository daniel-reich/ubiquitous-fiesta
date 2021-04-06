
def even_or_odd(s):
  even = 0
  odd = 0
  for i in range(len(s)):
    if int(s[i]) % 2 == 0:
      even += int(s[i])
    else:
      odd += int(s[i])
  if odd > even:
    return "Odd is greater than Even"
  elif even > odd:
    return "Even is greater than Odd"
  else:
    return "Even and Odd are the same"

