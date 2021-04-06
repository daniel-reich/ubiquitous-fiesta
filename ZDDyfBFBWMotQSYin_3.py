
def is_harshad(num):
  l = list(str(num))
  a = sum([int(e) for e in l])
  if a == 0:
    return False
  if num % a == 0:
    return True
  else:
    return False

