
def how_bad(n):
  result = []
  population = bin(n)[2:].count('1')
  if not population % 2:
    result.append('Evil')
  else:
    result.append('Odious')
  prime = True
  if population == 1:
    return result
  for num in range(2, population):  
    if not population % num:
      prime = False
      break
  if prime:
    result.append('Pernicious')
  return result

