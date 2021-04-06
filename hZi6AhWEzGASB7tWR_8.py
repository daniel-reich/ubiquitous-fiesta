
def isIncreasing(lst):
  for i in range(len(lst)-1):
    if lst[i]>=lst[i+1]: return False
  return True
def isDecreasing(lst):
  for i in range(len(lst)-1):
    if lst[i]<=lst[i+1]: return False
  return True
def check(lst):
  if isIncreasing(lst): return "increasing"
  if isDecreasing(lst): return "decreasing"
  return "neither"

