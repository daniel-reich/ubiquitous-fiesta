
def era(er, ip):
  full_ip = round(ip)
  ip = full_ip + (ip - full_ip)*10/3.
  return '%.2f' % (9 * er / ip)

