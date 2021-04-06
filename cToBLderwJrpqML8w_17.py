
def champions(teams):
  compare = lambda x: (x['wins']*3 + x['draws'], x['scored']-x['conceded'])
  return max(teams, key=compare)['name']

