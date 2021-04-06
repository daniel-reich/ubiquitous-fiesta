
def split(num):
  q = num//3
  r = num%3
  if num == 1:
    return 1
  if r == 0:
    return 3**q
  if r == 1:
    return 3**(q-1)*4
  if r == 2:
    return 3**q*2

