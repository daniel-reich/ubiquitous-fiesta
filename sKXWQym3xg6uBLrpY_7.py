
def median(lst):
  if len(lst) % 2 == 1:
    return lst[len(lst)//2]
  return (lst[len(lst)//2 - 1] + lst[len(lst)//2]) / 2
​
def iqr(lst):
  lst.sort()
  left, right = lst[:len(lst)//2], lst[-(len(lst)//2):]
  return median(right) - median(left)

