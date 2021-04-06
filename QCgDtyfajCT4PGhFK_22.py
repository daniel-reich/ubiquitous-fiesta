
def prime_factorization(number):
  if number == 1:
    return []
  lst = []
  i = 2
  while(i<=number and i > 1):
    if number % i == 0:
      number /= i
      lst.append(i)
      i = 2
      continue
    i += 1
  return lst

