
def largest_even(lst):
  max=0
  for i in lst:
    if i%2==0 and i>max:
      max=i
  if max==0:
    return -1
  return max

