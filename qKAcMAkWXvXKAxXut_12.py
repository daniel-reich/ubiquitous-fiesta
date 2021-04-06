
def calc_bundled_temp(n, temp):
  temp = int(temp[:-2])
  for x in range(n):
    temp += 0.1 * temp
  
  return str(round(temp,1)) + '*C'

