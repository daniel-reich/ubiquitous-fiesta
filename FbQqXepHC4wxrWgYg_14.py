
def prime_divisors(num):
  divisors = set()
  i = 2
  while num > 1:
    while num % i == 0:
      divisors.add(i)
      num = num // i
    i += 1
  return sorted(divisors)

