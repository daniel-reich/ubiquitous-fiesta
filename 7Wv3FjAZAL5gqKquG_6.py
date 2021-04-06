
def era(er, ip):
  if ip % 1 == 0:
    return '%.2f' % (er/ip*9)
  remainder = ip % 1
  base = ip // 1
  remainder *= 3
  ip = base + remainder
  return '%.2f' % (er/ip*9)

