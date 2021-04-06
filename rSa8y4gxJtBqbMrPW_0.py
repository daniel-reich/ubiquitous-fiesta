
def lcm(n1, n2):
  i = max(n1, n2)
  while i%n1 or i%n2:
    i += 1  
  return i

