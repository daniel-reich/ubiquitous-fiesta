
def award_prizes(names):
  points = sorted(names.values(), reverse=True)
  for p in names:
    pix = points.index(names[p])
    names[p] = 'Gold' if pix == 0 else 'Silver' if pix == 1 else 'Bronze' if pix ==2 else 'Participation'
  return names

