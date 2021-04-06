
def calc_bundled_temp(n, temp):
  Ti = int(temp[:-2])
  Tf = Ti
  for i in range(n):
    Tf = Tf * 1.1
  Tf = round(Tf, 1)
  return(str(Tf) + "*C")

