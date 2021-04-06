
def complete_factorization(num):
  i = 2
  result = []
  while num >= i:
    if num % i == 0: 
      result.append(i)
      num = num // i
      i = 2
    else:
      i += 1
  return result

