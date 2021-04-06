
def sock_merchant(lst):
  pairs = 0
  for x in set(lst):
    while lst.count(x) >= 2:
      pairs += 1
      lst.remove(x)
      lst.remove(x)
  return pairs

