
def is_harshad(num):
  a = sum([int(x) for x in str(num)])
  if num == 0:
    return False
  elif num % a == 0:
    return True
  else:
    return False

