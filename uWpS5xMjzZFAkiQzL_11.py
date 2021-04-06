
def odds_vs_evens(num):
  odds = 0
  even = 0
  for digit in str(num):
    if int(digit) % 2 == 0: 
      even += int(digit)
    else:
      odds += int(digit)
  return "odd" if odds > even else( "even" if odds < even else "equal")

