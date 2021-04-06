
def every_some(test, val, a, b, c, d, e):
  candidates = list(map(str, [a, b, c, d, e]))
  if val == "everybody":
    return all([eval(i + test) for i in candidates])
  else:
    return any([eval(i + test) for i in candidates])

