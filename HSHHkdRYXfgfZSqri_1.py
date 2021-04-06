
def damage(d, s, t):
  return d * s * {'s':1,'m':60,'h':3600}[t[0]] if d>0 and s>0 else 'invalid'

