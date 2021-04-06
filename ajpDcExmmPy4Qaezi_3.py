
def EPLResult(table, team):
  s = sorted(table, key=lambda x: (x[2] * 3 + x[3], x[5]), reverse=True)
  i = 0
  for x in range(len(s)):
    if s[x][0] == team:
      i = x
      break
  p = i + 1
  t = s[i]
  pos = 'st' if p == 1 else 'nd' if p == 2 else 'rd' if p == 3 else 'th'
  return "{} came {}{} with {} points and a goal difference of {}!".format(team, p, pos,t[2] * 3 + t[3], t[5])

