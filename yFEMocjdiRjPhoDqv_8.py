
def prime_in_range(n1, n2):
  return any(True for i in range(n1, n2+1) if 1 == sum(not i % j for j in range(1,i)))

