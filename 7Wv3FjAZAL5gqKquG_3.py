
def era(er, ip):
  if ip==int(ip): return '%.2f' % ((9*er)/ip)
  elif ip==int(ip)+0.1: return '%.2f' % ((27*er)/(3*int(ip)+1))
  else: return '%.2f' %  ((27*er)/(3*int(ip)+2))

