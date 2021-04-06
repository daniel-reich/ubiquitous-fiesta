
def era(er, ip):
  ip = ip//1 + (ip % 1)*10/3
  return (str(round(er*9/ip,2)) + '00')[:4]

