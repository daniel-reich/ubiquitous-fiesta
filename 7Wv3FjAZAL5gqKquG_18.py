
def era(er, ip):
  if "." in str(ip):
    if ".1" in str(ip):
      ip = int(ip) + 1/3
    if ".2" in str(ip):
      ip = int(ip) + 2/3
  return "{0:.2f}".format(float(9 * (er / ip)))

