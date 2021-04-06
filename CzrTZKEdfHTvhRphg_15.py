
def mixed_number(frac):
  slash = frac.find("/")
  num = int(frac[:slash])
  dem = int(frac[slash+1::])
  if num == 0:
    return "0"
  elif num % dem == 0:
    return str(num // dem)
  elif abs(num) == 1:
    return frac
  else:
    n = abs(num)
    d = abs(dem)
    w = n // d
    factors = [i for i in range(1,min(n,d)) if n % i == 0 and d % i == 0]
    gcd = factors[-1]
    if gcd == 1 and n < d:
      return frac
    else:
      n = n // gcd
      d = d // gcd
      if num < 0:
        w = -1 * w
      if abs(num) < abs(dem):
        return "{}/{}".format(str(n % d), str(d))
      else:
        return "{} {}/{}".format(str(w), str (abs(n % d)), str(d))

