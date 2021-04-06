
def squares_sum(n):
  for n1 in range(int(n**0.5)+1):
    n1 *= n1
    n2 = (n-n1)**0.5
    if n2 == int(n2):
      return True
  return False

