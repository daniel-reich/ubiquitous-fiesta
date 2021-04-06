
def calc_bundled_temp(n, temp):
  num = int(temp[:-2])
  for i in range(n):
    num = num*1.1
  return str(round(num,1)) + '*C'

