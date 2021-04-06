
def balanced(lst):
  a = 0
  b = 0
  c = []
  num = int(len(lst)/2)
  for i in range(num):
    a += lst[i]
    b += lst[num+i]
  for i in range(num):
    if a >= b:
      c.append(lst[i])
    else:
      c.append(lst[num+i])
  for i in range(num):
    if a > b:
      c.append(lst[i])
    else:
      c.append(lst[num+i])
  return c

