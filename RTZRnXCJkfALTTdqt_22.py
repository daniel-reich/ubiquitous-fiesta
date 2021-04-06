
def sum_neg(lst):
  l = []
  if len(lst)== 0:
    return l
  count = 0
  sum1 = 0
  for x in lst:
    if x > 0:
      count += 1
    else:
      sum1 += x
  l.append(count)
  l.append(sum1)
  return l

