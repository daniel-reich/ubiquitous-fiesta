
def is_powerful(n):
  divisors = [a for a in range(1, n) if n % a == 0]
  pdiv = [a for a in divisors if len([i for i in range(1, a+1) if a % i == 0]) == 2]
  count = 0
  for i in pdiv:
    if i**2 not in divisors:
      count += 1
  return count == 0

