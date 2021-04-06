
def happiness_number(s):
  a = s.count(":)")
  b = s.count(":(")
  c = s.count("(:")
  d = s.count("):")
  return a - b + c - d

