
def largest_even(lst):
  large = -1
  for i in lst:
    if i > large and i % 2 == 0:
      large = i
  return large

