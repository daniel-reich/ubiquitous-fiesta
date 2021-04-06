
def one_odd_one_even(n):
  l = list(str(n))
  n1 = 0
  for i in range(0,len(l)):
    if int(l[i]) % 2 == 0:
      n1 += 1
  if n1 == 1:
    return True
  else:
    return False

