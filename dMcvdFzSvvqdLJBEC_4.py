
def num_of_days(cost, savings, start):
  money = cost-savings
  count = 0
  for i in range(1000):
    for j in range(7):
      money = money-(start+i+j)
      count += 1
      if money<=0:
        return count
  return count

