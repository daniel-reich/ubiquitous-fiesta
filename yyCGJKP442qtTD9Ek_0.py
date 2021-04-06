
def sums_of_powers_of_two(n):
  res, binary = [], bin(n)[2:]
  
  for idx, i in enumerate(reversed(binary)):
    if i == '1':
      res.append(2 ** idx)
  return res

