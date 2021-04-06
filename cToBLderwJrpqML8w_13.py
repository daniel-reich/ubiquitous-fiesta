
def champions(teams):
  t = [(x['wins']*3+x['draws'],x['scored']-x['conceded'],x['name']) for x in teams]
  return sorted(t)[-1][2]

