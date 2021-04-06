
def largest_even(lst):
  max = -1
  for i in lst:
    if i > max and not i % 2: max = i
  return max

