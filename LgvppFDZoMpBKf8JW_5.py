
def digital_clock(s):
  t = [s // 3600 % 24, s % 3600 // 60, s % 3600 % 60]
  return ':'.join(('0' + str(x))[-2:] for x in t)

