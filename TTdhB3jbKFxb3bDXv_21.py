
def left_shift(lst, n):
  length = len(lst)
  if length == n or n == 0:
    return lst
  for _ in range(n):
    lst.append(lst[0])
    lst = lst[1:]
  return lst
​
def right_shift(lst, n):
  length = len(lst)
  if length == n or n == 0:
    return lst
  for _ in reversed(range(n)):
    lst.insert(0, lst[-1])
    lst = lst[:-1]
  return lst

