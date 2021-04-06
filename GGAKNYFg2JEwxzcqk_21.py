
def anti_divisors(n):
  result = []
  for x in range(1,n):
    if n % x != 0:
      if x % 2 == 0 and (n*2) % x == 0:
        result.append(x)
      elif x % 2 != 0 and (((n*2)-1) % x == 0 or ( (n*2)+1) % x ==0):
        result.append(x)
  return result

