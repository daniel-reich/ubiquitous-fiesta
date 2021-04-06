
def award_prizes(names):
  names = sorted(names, key = lambda x: names[x], reverse = True)
  pleces = ['Bronze', 'Silver', 'Gold']
  d = {}
  for x in names:
    d[x] = pleces.pop() if pleces else 'Participation'
  return d

