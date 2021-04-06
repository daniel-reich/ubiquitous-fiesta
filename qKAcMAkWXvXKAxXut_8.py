
def calc_bundled_temp(n, temp):
  a=list(temp)
  b=a[:-2]
  d=eval("".join(b))
  c=round(d*(1.1**n),1)
  return "{}*C".format(c)

