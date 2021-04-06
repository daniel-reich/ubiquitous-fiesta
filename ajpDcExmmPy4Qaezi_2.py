
def EPLResult(table, team):
  t=sorted(table, key=lambda x: (x[2]*3+x[3], x[-1]), reverse=True)
  p=[x+[t.index(x)] for x in t]
  d={x[0]:x[1:] for x in p}
  pts=d[team][1]*3+d[team][2]
  ordinal=lambda i: '{}'.format('tsnrhtdd'[(i//10%10!=1)*(i%10<4)*i%10::4])
  rank='{}{}'.format(d[team][-1]+1, ordinal(d[team][-1]+1))
  gd=d[team][-2]
  res="{} came {} with {} points and a goal difference of {}!".format(team, rank, pts, gd)
  return res

