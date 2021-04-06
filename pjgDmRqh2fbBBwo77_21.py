
def has_syncopation(s):
  res = []
  for k in range(1, len(s), 2):
    if s[k] == "#":
      res.append(k)
  return len(res) > 0

