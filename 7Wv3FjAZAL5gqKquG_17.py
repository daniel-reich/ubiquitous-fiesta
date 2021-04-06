
def era(er, ip):
  if isinstance(ip, float):
    return str(round((er/(ip + 0.33))*9,2))
  else:
    return "{:.2f}".format(round((er/(ip))*9,2))

