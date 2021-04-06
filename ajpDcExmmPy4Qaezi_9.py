
def EPLResult(table, team):
  s = ('th', 'st', 'nd', 'rd') + ('th',)*10
  sorted_team = sorted(table, key = lambda x: (x[2] * 3 + x[3], x[-1]), reverse = True)
  place, pnts, g_diff = [[index + 1, row[2] * 3 + row[3], row[-1]] for index, row in enumerate(sorted_team) if row[0] == team][0]
  v = place % 100
  return '{} came {}{} with {} points and a goal difference of {}!'.format(team, place, s[v% 10] if v > 13 else s[v], pnts, g_diff)

