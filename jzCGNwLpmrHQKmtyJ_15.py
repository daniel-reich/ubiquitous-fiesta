
def parity_analysis(num):
  if num % 2 == 0:
    erg1 = True
  else:
    erg1 = False
  
  check = [int(i) for i in str(num)]
  print(check)
  erg2 = 0
  for i in check:
    erg2 += i
  if erg2 % 2 == 0:
    erg2 = True
  else:
    erg2 = False
    
  if erg2 == erg1:
    return True
  else:
    return False

