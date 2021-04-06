
def is_slidey(n):
  num = str(n)
  for i in range(1, len(num)):
    a = str(num[i - 1])
    b = str(num[i])
    aa = int(a)
    bb = int(b)
    dif = abs(aa - bb)
    if dif != 1:
      return False
  return True

