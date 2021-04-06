
def odds_vs_evens(num):
  lst = list(str(num))
  odd = 0
  even = 0
  for nr in lst:
    if int(nr) % 2 == 0:
      even = even + int(nr)
    else:
      odd = odd + int(nr)
  if odd > even:
    return "odd"
  elif odd < even:
    return "even"
  else:
    return "equal"

