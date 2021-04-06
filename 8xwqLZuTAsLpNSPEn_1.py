
def award_prizes(names):
  points = sorted(names.values())
  prizes = ['Participation']*(len(names)-3) + ['Bronze','Silver','Gold']
  d = dict(zip(points, prizes))
  return {n:d[p] for n,p in names.items()}

