
def expensive_orders(d, k):
  dic = {}
  for i, j in d.items():
    if j > k:
      dic[i] = j
  return dic

