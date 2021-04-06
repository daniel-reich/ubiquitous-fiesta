
def num_of_days(cost, savings, start):
  days = 0
  while True:
    for i in range(start, start+7):
      if savings < cost: days += 1; savings += i
      else: return days
    start += 1

