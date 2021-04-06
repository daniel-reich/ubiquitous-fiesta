
def EPLResult(table, team):
  season = [[t[0],3*t[2]+t[3],t[5]] for t in table]
  season.sort(key=lambda x:(x[1],x[2]))
  res = [(len(table)-e,t) for e,t in enumerate(season) if team==t[0]].pop()
  place = str(res[0])+('st' if res[0]==1 else 'nd' if res[0]==2 else 'rd' if res[0]==3 else 'th')
  return '{0} came {1} with {2} points and a goal difference of {3}!'.format(res[1][0],place,res[1][1],res[1][2])

