
def fact(num, total=1):
  return fact(num - 1, num * total) if num else total
​
def grid_pos(lst):
  return fact(sum(lst)) / fact(lst[0]) / fact(lst[1])

