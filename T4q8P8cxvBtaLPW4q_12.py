
def is_prime(num):
  count = 0
  for i in range(1, num+1):
    if num % i == 0:
      count += 1
  return count == 2
​
def extract_primes(num):
  primes = []
  for i in range(len(str(num))):
    for j in range(i + 1, len(str(num))+1):
      if is_prime(int((str(num))[i:j])) and int((str(num))[i]) != 0:
        primes.append(int((str(num))[i:j]))
  return sorted(primes)

