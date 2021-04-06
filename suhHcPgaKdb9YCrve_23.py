
def even_or_odd(s):
  if sum(int(x) for x in s if int(x) % 2 == 0) > sum(int(x) for x in s if int(x) % 2 == 1):
    return "Even is greater than Odd"
  elif sum(int(x) for x in s if int(x) % 2 == 0) < sum(int(x) for x in s if int(x) % 2 == 1):
    return "Odd is greater than Even"
  else:
    return "Even and Odd are the same"

