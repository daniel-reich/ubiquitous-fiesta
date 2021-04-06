
def award_prizes(names):
​
  l = sorted(names, key=lambda x: names[x], reverse=True)
​
  for k in names.keys():
​
    if k in l[:3]:
      names[k] = ['Gold', 'Silver','Bronze'][l.index(k)]
    else:
      names[k] = 'Participation'
​
  return names

