
def multiply(n1, n2):
  sum = 0
  for _ in range(abs(n2)):
    sum += abs(n1)
  if n1 < 0 and n2 > 0 or n1 > 0 and n2 < 0:
     return -sum
  return sum

