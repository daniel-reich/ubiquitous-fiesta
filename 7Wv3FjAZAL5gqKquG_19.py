
def era(er, ip):
  era = int(er/ip*9*100)/100
  eras = str(era)
  dig = len(eras.split('.')[1])
  return ''.join([eras, (2-dig)*'0'])

