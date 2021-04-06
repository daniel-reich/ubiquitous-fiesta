
def num_of_days(cost, savings, start):
  week = 0
  target = cost-savings
  while (7 * start + 21) * week + week*(week-1) / 2 * 7 < target:
    week += 1
  week -= 1
  day = 0
  target -= (7 * start + 21) * week + week*(week-1) / 2 * 7 
  while (start + week) * day + day * (day -1)/2 <= target:
    day += 1
  return 7 * week + day

