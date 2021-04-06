
def block(lst):
  result = 0
  for i in range(len(lst) - 1):
    if 2 in lst[i]:
      result += (len(lst) - i - 1) * lst[i].count(2)
  return result

