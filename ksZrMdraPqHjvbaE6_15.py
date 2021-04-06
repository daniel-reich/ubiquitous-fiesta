
def largest_even(lst):
  evenlst = []
  for i in lst:
    if i % 2 == 0:
      evenlst.append(i)
  evenmax = -1
  for i in evenlst:
    if i > evenmax:
      evenmax = i
      
  return evenmax

