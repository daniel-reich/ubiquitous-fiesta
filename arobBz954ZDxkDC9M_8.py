
def next_prime(num):
  while 1:
    if is_prime(num): return num
    else: num += 1 
    
def is_prime(num):
  return all([num % i != 0 for i in range(2, num, 1)])

