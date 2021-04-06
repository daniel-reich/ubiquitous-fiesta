
def doubleton(n):
  lst = []
  while True:
    n += 1
    for i in str(n):
      if i not in lst:
        lst.append(i)
    if len(lst) == 2:
      break
    else:
      lst = []
  return n

