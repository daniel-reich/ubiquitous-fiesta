
def steps_to_convert(txt):
  s = sum(1 for c in txt if c.isupper())
  s_ = sum(1 for c in txt if c.islower())
  if txt.isupper() or txt.islower():
    return 0
  if s>s_:
    return s_
  elif s<s_:
    return s
  else:
    return s

