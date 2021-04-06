
def consecutive_sum(n):
  return n%2 or bool([x for x in range(2,n) if n%x==0 and x%2])

