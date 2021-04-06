
def is_repdigit(num):
  if (num < 0): return False
  else:
    a = num % 10
    num = num // 10
    while ((num > 0)):
      b = num % 10
      if (a != b):
        return False
      a = b
      num = num // 10
    return True

