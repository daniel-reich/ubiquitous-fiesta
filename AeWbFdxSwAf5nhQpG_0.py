
def persistence(num):
  i = 0
  while len(str(num)) > 1 and i < 50:
    num = eval('*'.join(str(num)))
    i += 1
  return i

