
def i_sqrt(n):
  count = 0
  if n < 0:
    return "invalid"
  else:
    while n >= 2:
      n = n ** (1/2)
      count += 1
  return count

