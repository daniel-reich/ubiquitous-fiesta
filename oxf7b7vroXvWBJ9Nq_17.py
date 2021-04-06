
def discount(n, txt):
  discs = txt.split(", ") if txt else ['0']
  add_disc = [eval(d) for d in discs if '%' not in d]
  mult_disc = [1-eval(d[:-1])/100 for d in discs if '%' in d]
  for m in mult_disc:
    n*= m
  for a in add_disc:
    n-= a
  return round(n,2)

