
def float_sum(a, b):
  multi = sorted([len(str(float(a)).split(".")[1]), len(str(float(b)).split(".")[1])])[-1]
  newa = (a * int(("1" + "0" * multi)))
  newb = (b * int(("1" + "0" * multi)))
  return (newa + newb) / int("1" + "0" * multi)

