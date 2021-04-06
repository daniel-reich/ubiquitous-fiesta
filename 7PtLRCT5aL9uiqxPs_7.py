
def last_dig(a, b, c):
  x1 = a%10
  x2 = b%10
  x3 = c%10
  a = (x1*x2)%10
  if a == x3: 
    return True
  else:
    return False
  '''if n3 == a:
    return True
  else:
    return False'''

