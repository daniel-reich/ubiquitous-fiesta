
def gcd(lst):
  minnum = min(lst)
  newlist = []
  factor = False
  count = 0
  for i in range(1,minnum+1):
    for eachnumber in lst:
      if eachnumber % i == 0:
        count += 1
        continue
    if count == len(lst):
      newlist.append(i)
      count = 0
    else:
      count = 0
  return max(newlist)

