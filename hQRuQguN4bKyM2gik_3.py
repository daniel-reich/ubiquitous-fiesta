
def simple_check(a, b):
  [a,b],c=sorted([a,b]),0
  while a and b:
    c+=not b%a
    a-=1
    b-=1
  return c

