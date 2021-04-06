
def sock_merchant(lst):
  count = 0
  num = [lst.count(l) for l in set(lst) if lst.count(l) > 1]
  for n in range(len(num)):
    while num[n] >= 2:
      num[n] /= 2
      count += 1
  return count

