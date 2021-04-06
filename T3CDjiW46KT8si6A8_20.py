
def product(lst):
  if lst[1:] == lst[:-1]:
    return lst[0]*lst[1]
​
  num1 = max(lst)
  box = []
​
  for i in lst:
    if i == num1:
      continue
    else:
      box.append(i)
  return max(box) * num1

