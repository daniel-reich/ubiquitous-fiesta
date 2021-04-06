
def simplify_frac(f):
  parts = f.split('/')
  den = int(parts[0])
  num = int(parts[1])
  gcd_val = gcd(den,num)
  if gcd_val == 1:
    return f
  else:
    den = int(den / gcd_val)
    num = int(num / gcd_val)
    return str(den) + "/" + str(num)
  
def gcd(a,b):
  if b == 0:
    return a
  else:
    return gcd(b, a % b)

