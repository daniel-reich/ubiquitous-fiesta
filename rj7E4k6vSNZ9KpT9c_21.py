
def factor_chain(lst):
  lst1 = []
  for x in lst:
    if lst[-1] % x == 0:
      lst1.append(x)
  return len(lst) == len(lst1)

