
def num_of_days(cost, savings, start):
  cost = cost-savings
  if cost < 1:
    return 0
  d = 0
  while cost > 0:
    for i in range(7):
      cost -= (start + i)
      d += 1
      if cost < 1:
        break
    start += 1
  return d

