
def how_bad(n):
  result = []
  pop = bin(n).count('1')
  if pop % 2:
    result.append('Odious')
  else:
    result.append('Evil')
  if pop == 1: return result
  for i in range(2,pop):
    if pop % i == 0:
      break
  else:
    result.append('Pernicious')
  return result

