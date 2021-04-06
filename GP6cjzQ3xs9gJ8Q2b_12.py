
def is_polydivisible(n):
  int_len = len(str(n))
  str_n = str(n)
  for i in range(1, int_len+1):
    if int(str_n[:i]) % i != 0: 
      return False 
  return True

