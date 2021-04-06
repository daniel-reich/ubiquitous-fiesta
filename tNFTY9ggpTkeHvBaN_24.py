
def prod(*args):
  result = 1
  for arg in args:
    result *= arg
  return result
​
def add(*args):
  result = 0
  for arg in args:
    result += arg
  return result
​
def total_volume(*boxes):
  return add(*(prod(*box) for box in boxes))

