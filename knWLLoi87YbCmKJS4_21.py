
def next_number(n):
  return sum([int(x)**2 for x in str(n)])
def happy(n):
  if n==1:
    return True
  if n==4:
    return False
  return happy(next_number(n))

