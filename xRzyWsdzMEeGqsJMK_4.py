
def maskify(txt):
  if len(txt) >= 4:
    return '#'*(len(txt)-4) + txt[-4:]
  return txt

