
def odds_vs_evens(num):
  odd_lst = []
  even_lst = []
  x = [int(x) for x in str(num)]
  for i in x:
    if i % 2 == 0:
      even_lst.append(i)
    else:
      odd_lst.append(i)
  if sum(odd_lst) > sum(even_lst):
    return "odd"
  elif sum(even_lst) > sum(odd_lst):
    return "even"
  else:
    return "equal"

