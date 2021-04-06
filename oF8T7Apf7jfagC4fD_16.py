
def antipodes_average(lst): #w/o built-in
  def l(arr):
    count = 0
    while arr != []:
      count += 1
      arr = arr[1:]
    return count
  if l(lst) % 2:
    a, b = lst[:l(lst)//2], lst[l(lst)//2 + 1:][::-1]
  else:
    a, b = lst[:l(lst)//2], lst[l(lst) // 2:][::-1]
  res = [None] * (l(a) + l(b))
  res[::2], res[1::2], i, new, count = a, b, [], [], 0
  for x in res:
    i += [x]
    count += 1
    if count == 2:
      new += [i]
      count = 0
      i = []
  return [x / 2 for x in [x[0] + x[1] for x in new]]

