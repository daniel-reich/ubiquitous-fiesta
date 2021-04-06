
def func_sort(lst):
  res = []
  times = 0
  for item in lst:
    while True:
      try:
        if callable(eval('item{}'.format('()'*(times+1)))):
            times += 1
        else: res.append(times + 1); break
      except:
        res.append(times); break
    times = 0
  return sorted(lst, key=lambda item: res[lst.index(item)])

