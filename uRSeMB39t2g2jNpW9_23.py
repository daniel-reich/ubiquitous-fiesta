
def turn_calc(num):
  l = ['O','I','Z','E','H','S','G','L','B']
  
  return ''.join(l[int(i)] for i in str(num).replace('.','')[::-1])

