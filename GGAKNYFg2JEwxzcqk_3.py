
def anti_divisors(n):
  return [x for x in range(1, n) if (n%x != 0 and x%2==0 and (n*2)%x==0) or (n%x != 0 and x%2!=0 and ((n*2+1)%x==0 or(n*2-1)%x==0)) ]

