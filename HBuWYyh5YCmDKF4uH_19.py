
def is_sorted(lst):
  return lst == sorted(lst) or lst == sorted(lst, reverse=True)
​
​
def almost_sorted(lst):
  if is_sorted(lst):
    return False
  else:
    return any(is_sorted(lst[:i] + lst[i+1:]) for i in range(len(lst)))

