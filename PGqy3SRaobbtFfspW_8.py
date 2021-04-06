
def simple_pair(lst, n):
  count1 = 0  
  count2 = 0
  for x in lst:
    if x == 0 or n % x != 0:
      count1 += 1
      continue
    else:
      y = int(n / x)
    for z in lst:
      if count1 != count2:
        if z == y:
          return [x, z]
      count2 += 1
    count2 = 0
    count1 += 1
  return None

