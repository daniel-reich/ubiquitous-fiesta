
def next_prime(num):
  if all(num % i for i in range(2, int(num**0.5) + 1)):
    return num
  else:
    return next_prime(num + 1)

