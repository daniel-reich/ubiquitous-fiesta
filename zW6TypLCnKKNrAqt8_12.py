
def left_side(lst):
  ans = [0]
  for i in range(0, len(lst) - 1):
    s = list(filter(lambda x: x < lst[i+1], lst[0:i+1]))
    ans.append(len(s))
  return ans
​
def right_side(lst):
  ans = []
  for i in range(0, len(lst) - 1):
    s = list(filter(lambda x: x < lst[i], lst[i+1:]))
    ans.append(len(s))
  ans.append(0)
  return ans

