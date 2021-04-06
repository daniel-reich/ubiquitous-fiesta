
def josephus(n):
  if n == 0:
    return False
  else:
    lst = []
    for i in range(n):
      lst.append(i)
    while len(lst) > 1:
      lst.remove(lst[1])
      lst.append(lst.pop(0))
  return lst[0]

