
def find(lst, value, start=0):
  for i in range(start, len(lst)):
    if lst[i] == value:
      return i
  return -1
  
def two_product(lst, n):
  for i in range(len(lst)):
    q, r = divmod(n, lst[i])
    if r == 0 and find(lst, q, i) > 0:
      return sorted([lst[i], q])
  return None

