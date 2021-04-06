
def simple_check(a, b):
  count = 0
  if a < b:
    while a != 0:
      if b % a == 0:
        count += 1
      a -= 1
      b -= 1
  else:
    while b!= 0:
      if a % b == 0:
        count += 1
      a -= 1
      b -=1
  return count

