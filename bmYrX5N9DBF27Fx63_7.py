
def greatest_impact(lst):
  # lst in format: [Mood, Weather, Meals, Sleep]
  d={'Weather':0, 'Meals':0, 'Sleep':0}
  for i in lst:
    d['Weather']+= abs(i[0]-i[1])
    d['Meals']+= abs(i[0]-i[2])
    d['Sleep']+= abs(i[0]-i[3])
  res=sorted(d,key=lambda x:d[x])
  return res[0] if d[res[0]]!=d[res[1]] else "Nothing"

