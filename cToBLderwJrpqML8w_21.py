
def champions(teams):
  rating = lambda t: (t['wins']*3 + t['draws'], t['scored'] - t['conceded'])
  return sorted(teams, key=rating, reverse=True)[0]['name']

