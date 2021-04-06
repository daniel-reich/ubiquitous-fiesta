
import re
def count_eatable_chocolates(total_money, cost_of_one_chocolate):
  regex = r"(-?\d+)"
  total = int(re.search(regex,total_money).group(1))
  cost = int(re.search(regex,cost_of_one_chocolate).group(1))
  if total <= 0 or cost <= 0:
    return "Invalid Input"
  start = total // cost
  counter = start
  while start >= 3:
    counter += start // 3
    start = start // 3 + start % 3
  return counter

