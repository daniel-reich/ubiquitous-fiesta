
def maskify(txt):
  if len(txt)<5: return txt
  return '#'*(len(txt)-4)+txt[-4:]

