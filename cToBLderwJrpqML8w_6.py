
def champions(teams):
  def points(d):
    return d['wins'] * 3 + d['draws']
  max_points = max([points(i) for i in teams])
  champs = [i for i in teams if points(i) == max_points]
  if len(champs) == 1:
    return champs[0]['name']
  return max(champs, key=lambda x: x['scored'] - x['conceded'])['name']

