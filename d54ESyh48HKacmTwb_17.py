
def gcd(lst):
  max_div = 1
  for i in range(2, min(lst)+1):
    not_ok = True
    for j in lst:
      if j % i != 0:
        not_ok = False
        break
    if not_ok:
      max_div = i
  return max_div

