
def simplify_frac(f):
  f_lst = f.split("/")
  numerator, denominator = int(f_lst[0]), int(f_lst[1])
  numer, denom = int(f_lst[0]), int(f_lst[1])
  while denom:
    numer, denom = denom, numer % denom
  return str((numerator // numer)) + "/" + str((denominator // numer))

