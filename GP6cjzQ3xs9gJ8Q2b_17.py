
def is_polydivisible(n, index = 0):
  if isinstance(n, str) == False:
    n = str(n)
  if index == len(n):
    return True
  
  tn = int(n[:index+1])
  td = index + 1
  
  if tn % td != 0:
    return False
  
  return is_polydivisible(n, td)

