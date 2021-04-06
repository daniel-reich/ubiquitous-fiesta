
def complete_factorization(num):
  #find biggest prime number below half of num
  prime_numbers = []
  i = num // 2 + 1
  while i > 2:
    prm = True
    for n in range(2, i):
      if i % n == 0:
        prm = False
    if prm:
      prime_numbers.append(i)
    i -= 1
  prime_numbers.append(2)
  result = []
  for p in prime_numbers:
    while num % p == 0:
      result.append(p)
      num = num // p
  if result == []:
    result.append(num)
  return result[::-1]

