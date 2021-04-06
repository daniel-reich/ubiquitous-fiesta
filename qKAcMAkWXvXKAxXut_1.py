
def calc_bundled_temp(n, temp):
  return str(round(int(temp.strip('*C'))*(1.1**n), 1))+'*C'

