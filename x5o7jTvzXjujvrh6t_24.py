
def i_sqrt(n):
  if n < 0:
    return "invalid"
  else:
    count = 0
    while n >= 2:
      n = n**0.5
      count = count + 1
    return count

