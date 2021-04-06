
def base_conv(n,b):
  base = { i: chr(ord('a')+i) for i in range(26)}
  rev = {v:k for k,v in base.items()}
  if type(n) == int:
    ret = []
    while n > 0:
      ret.append(base[n % b])
      n = n // b
    return "".join(ret[::-1])
  else:
    for c in n:
      if c not in rev or rev[c] >= b:
        return "{} is not a base {} number.".format(n, b)
    return sum(rev[c]*b**i for i,c in enumerate(n[::-1]))

