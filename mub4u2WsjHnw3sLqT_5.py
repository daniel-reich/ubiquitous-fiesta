
count = 0
​
def lambda_depth(num):
  global count
  count = num
  return second()
​
def second():
  global count
  if count > 0:
    count -= 1
    return second
  else:
    return "edabit"

