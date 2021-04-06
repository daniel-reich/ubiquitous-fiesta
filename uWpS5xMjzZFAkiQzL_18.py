
def odds_vs_evens(num):
  odds=0
  evens=0
  for i in str(num):
    if int(i)%2:
      odds += int(i)
    else:
      evens += int(i)
  return "odd" if odds > evens else "even" if evens > odds else "equal"

