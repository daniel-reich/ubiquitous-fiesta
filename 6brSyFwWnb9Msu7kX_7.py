
def pos_neg_sort(lst):
  sorted_lst = sorted(filter(lambda n: n >= 0, lst))
  s_i = 0
  res = []
  for i in range(len(lst)):
    if lst[i] < 0:
      res.append(lst[i])
    else:
      res.append(sorted_lst[s_i])
      s_i += 1
  return res

