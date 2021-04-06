
def prime_factorization(number):
  result = []
  for n in range(2,number):
    while number % n == 0:
      result.append(n)
      number /= n
  return result

