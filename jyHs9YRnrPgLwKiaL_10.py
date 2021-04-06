
def split(x):
  list = []
  for i in range(1, x+1):
    num = (x/i) ** i
    list.append(round(num, 1))
  list.sort()
  list.reverse()
  return list[0]

