
def turn_calc(num):
  convs = ['O','I','Z','E','H','S','G','L','B','-']
  return ''.join(convs[int(d)] for d in str(num).replace('.',''))[::-1]

