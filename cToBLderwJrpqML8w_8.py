
def TP(d):
  return 3 *d['wins'] + 0 * d['loss'] + 1 * d['draws']
def GD(d):
  return d['scored'] - d['conceded']
def champions(teams):
  T=sorted(teams, key=lambda x: (-TP(x), -GD(x)))
  return T[0]["name"]

