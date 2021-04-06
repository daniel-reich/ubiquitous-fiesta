
def min_swaps(string):
  digits, sl = [int(d) for d in string], len(string)
  swaps = lambda d: sum(digits[i] != (i+d)%2 for i in range(sl))
  return min(swaps(0), swaps(1))

