
def is_exactly_three(n):
  return is_prime(n**0.5) if not (n**0.5)%1 else False
  
def is_prime(n):
  return n>1 and all(n%i for i in range(2,int(n**0.5)+1))

