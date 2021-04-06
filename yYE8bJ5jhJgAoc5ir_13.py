
def bugger(num):
  mult = 0
  prod = num
  prd = 1
  if len(str(num)) == 1:
    return mult
  while len(str(prod)) != 1:
    prd = 1
    for number in str(prod):
      prd *= int(number)
    
    prod = prd
    mult += 1
    
  return mult

