
def odds_vs_evens(num):
  odds = 0
  evens = 0
  for c in str(num):
    if int(c) % 2 == 0:
      evens += int(c)
    else:
      odds += int(c)
  print(odds, ":", evens)
  if odds > evens:
    return "odd"
  elif odds == evens:
    return "equal"
  elif evens > odds:
    return "even"

