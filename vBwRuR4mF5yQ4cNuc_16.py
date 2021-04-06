
def count_missing_nums(lst):
  x = sorted(list([int(x) for x in lst if x.isdigit()]))
  total = 0
  for i in range(min(x),max(x)+1):
    if i not in x:
      total += 1
  return total

