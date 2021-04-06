
def calc_bundled_temp(n, temp):
  result = int(temp[:-2])
  for i in range(1, n+1):
    result = result*1.1
    
    
  return str(round(result, 1)) + '*C'

