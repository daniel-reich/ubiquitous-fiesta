
def standard_deviation(lst):
  a = sum(lst)/len(lst)
  new_lst = []
  for i in lst:
    new_lst.append((i - a) ** 2)
  return round((sum(new_lst)/len(new_lst)) ** .5, 2)

