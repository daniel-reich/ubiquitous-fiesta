
def prime_divisors(num):
  divisors=[d for d in range(2,num//2+1) if num%d==0]
  return [d for d in divisors if all(d%od!=0 for od in divisors if od!=d)]

