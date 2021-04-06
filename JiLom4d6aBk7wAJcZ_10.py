
def is_sastry(n):
  return int("".join([str(n),str(n+1)]))**0.5%1==0

