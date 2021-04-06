
def is_equal(lst):
  total = []
  for x in lst:
    totalsum = 0
    for y in str(x):
      totalsum += int(y)
    total.append(totalsum)
  if len(total) == total.count(total[0]):
    return True
  else:
    return False

