
def simplify_frac(f):
  def gcd(a,b):
    if b== 0:
      return a
    return gcd(b,a%b)
  a,b = f.split('/')
  c = gcd(int(a),int(b))
  return "{}/{}".format(int(int(a)/c),int(int(b)/c))

