
def uncensor(t, v):
  for c in v: t = t.replace('*', c, 1)
  return t

