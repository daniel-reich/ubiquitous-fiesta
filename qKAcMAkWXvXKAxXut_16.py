
def calc_bundled_temp(n, temp):
  return '{}*C'.format(round(int(temp[:-2]) * 1.1 ** n, 1))

