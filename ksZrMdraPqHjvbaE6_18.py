
def largest_even(lst):
  temp = -1
  for x in lst:
    if x % 2 == 0 and x > temp:
      temp = x
  return temp

