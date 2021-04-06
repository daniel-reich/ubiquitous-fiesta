
import re
def day_of_year(date):
  nums = re.findall(r'\d+',date)
  m,d,y = int(nums[0]),int(nums[1]),int(nums[2])
  days = [31,28,31,30,31,30,31,31,30,31,30,31]
  if m == 1:
    return d
  if m == 2:
    return 31 + d
  if y % 4 == 0:
    if y % 100 == 0:
      if y % 400 == 0:
        days[1] = 29
    else:
      days[1] = 29
  return sum(days[:m-1]) + d

