
def pirates_killed(gold, tolerance):
  diff = []
  res = []
  for num in gold:
    diff.append(max(gold) - num)
  distribution = set(zip(diff, tolerance))
  for i in distribution:
    res.append(i[0] > i[1])
    
  return any(res)

