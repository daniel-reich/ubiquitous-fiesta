
def sum_digits(n):
  if n:
    c=0
    while n>0:
      n//=10
      c+=1
    return c
  return 1

