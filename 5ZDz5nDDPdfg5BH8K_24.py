
def check(start, target):
  if start == target:
    return True
  elif start > target:
    return False
    
  return check(start*3, target) or check(start+5, target)
​
def only_5_and_3(n):
  return check(3, n) or check(5, n)

