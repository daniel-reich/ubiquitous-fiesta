
def isincreasing(lst):
  if len(lst)==1:
    return True
  if lst[0]>=lst[1]:
    return False
  return isincreasing(lst[1:])
def isdecreasing(lst):
  if len(lst)==1:
    return True
  if lst[0]<=lst[1]:
    return False
  return isdecreasing(lst[1:])
​
​
def check(lst):
  if isincreasing(lst):
    return "increasing"
  if isdecreasing(lst):
    return "decreasing"
  return "neither"

