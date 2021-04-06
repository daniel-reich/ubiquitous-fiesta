
def how_bad(n):
  result = []
  ones = bin(n).count('1')
  print(ones)
  print(bin(n))
  if ones % 2:
    result.append('Odious')
  else: 
    result.append('Evil')
  isPrime = True
  for x in range (2,ones):
    if ones % x == 0:
      isPrime = False
  if isPrime and ones > 1:
    result.append('Pernicious')
  return result

