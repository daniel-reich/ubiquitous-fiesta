
def is_prime(num):
  return not(any(i for i in range(2,int(num**0.5)+1) if num%i == 0)) if num != 1 else False

