
def next_prime(num):
  if num % 2 != 0 and 0 not in [num % i for i in range(2, num)]:
    return num
  else:
    return next_prime(num + 1)

