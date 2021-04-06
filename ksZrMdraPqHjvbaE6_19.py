
def largest_even(lst):
  hi = 0
  for n in lst:
    if n % 2 == 0 and n > hi: 
      hi = n
  return hi if hi else -1

