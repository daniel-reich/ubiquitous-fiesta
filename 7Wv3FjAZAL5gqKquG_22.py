
def era(er, ip):
  ip = int(ip) + 2/3 if ip == int(ip) + 0.2 else int(ip) + 1/3 if ip == int(ip) + 0.1 else ip
  return '{:4.2f}'.format(round(9 * er / ip, 2))

