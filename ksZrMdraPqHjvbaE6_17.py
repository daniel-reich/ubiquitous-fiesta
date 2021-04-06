
def largest_even(lst):
  m = -1
  for x in lst:
    if x % 2 == 0:
      if x > m:
        m = x
  return m

