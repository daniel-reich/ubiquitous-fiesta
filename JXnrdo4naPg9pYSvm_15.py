
def frac_round(frac, n):
  num, den = frac.split("/")[0], frac.split("/")[-1]
  deci = int(num) / int(den)
  deci = round(deci, n)
  while len(str(deci).split(".")[-1]) < n:
      deci = str(deci)
      deci += "0"
  return "{} rounded to {} decimal places is {}".format(frac, n, deci)

