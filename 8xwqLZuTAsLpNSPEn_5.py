
def award_prizes(names):
  fin = {}
  prizes = ['Gold', 'Silver', 'Bronze'] + (['Participation'] * (len(names)-3))
  ranked = [k for k,v in sorted(names.items(), key=lambda x: x[1],reverse=True)]
  awards = [(b, prizes[a]) for a, b in enumerate(ranked)]
  for a in names:
    for b in awards:
      if a==b[0]: fin[a]=b[1]
  return fin

