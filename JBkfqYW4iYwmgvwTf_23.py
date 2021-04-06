
def is_prime(num):
  return num > 1 and not any(True for x in range(2, num // 2) if num % x == 0)

