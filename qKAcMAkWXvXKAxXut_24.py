
def calc_bundled_temp(n, temp):
  ntemp = int(temp[:-2])
  total = round((ntemp * (1.1 ** n)), 1)
  txt = str(total) + "*C"
  return txt

