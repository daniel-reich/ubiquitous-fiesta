
def era(er, ip):
  s = str(ip)
  l = len(s)
  n = s.find('.')
  denom = ip
  if n > 0 and n != l - 1:
    denom = int(s[:n]) + int(s[-1]) / 3
  return '{:.2f}'.format(er / denom * 9)

