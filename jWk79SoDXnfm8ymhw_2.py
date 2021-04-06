
def censor(s):
  for i in s.split():
    if len(i) > 4:
      s = s.replace(i, "*" * len(i))
  return s

