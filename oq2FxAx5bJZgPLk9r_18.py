
def sock_merchant(lst):
  pairs = 0
  for i in set(lst):
    pairs+=lst.count(i)//2
  return pairs

