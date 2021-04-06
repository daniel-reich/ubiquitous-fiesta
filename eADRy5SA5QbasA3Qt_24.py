
def is_harshad(n):
  a = 0
  for i in str(n):
    a += int(i)
  if n % a == 0:
    return True
  else:
    return False

