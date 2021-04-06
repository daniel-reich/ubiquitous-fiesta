
def frac_round(frac, n):
  (x, y) = frac.split("/")
  form = "{:." + str(n) + "f}"
  deci = form.format(round(int(x) / int(y), n))
  string = frac + " rounded to " + str(n) + " decimal places is " + str(deci)
  return string

