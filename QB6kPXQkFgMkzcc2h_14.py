
def remove_abc(txt):
  s = "".join(c for c in txt if c not in "abcABC")
  if s == txt:
    return None
  return s

