
def era(er, ip):
  if ip == 99.1: ip = 99+(1/3)
  elif ip == 99.2: ip = 99+(2/3)
  ret = str(round(er*9/ip,2))
  if len(ret) == 3: ret+="0"
  return ret

