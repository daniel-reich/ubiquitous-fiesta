
def guess_score(code, gues):
  d_code = {k:code.count(k) for k in code}
  d_gues = {k:gues.count(k) for k in gues}
  raw = sum(min(d_gues.get(v), d_code.get(v,0)) for v in d_gues)
  black = sum(g==c for g,c in zip(gues, code))
  white = raw - black
  return {"black": black, "white": white}

