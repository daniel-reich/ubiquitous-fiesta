
def is_prime(num):
  return all(num%i!=0 for i in range(2, int(num**0.5)+1)) if num>1 else False

