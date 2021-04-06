
def pentagonal(num):
  u = 1
  l = 0
  for i in range(1,num):
    l += 5
    u += l
  return u

