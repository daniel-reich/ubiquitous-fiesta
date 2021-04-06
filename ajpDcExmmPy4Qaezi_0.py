
fstr = "{} came {}{} with {} points and a goal difference of {}!"
​
def EPLResult(table, team):
  points = lambda result: result[2]*3 + result[3]
  suffix = lambda pos: ["th", "st", "nd", "rd"][pos%20 if pos%20 in [1,2,3] else 0]
​
  final = sorted(table, key=lambda res: (-points(res), -res[5]))
  idx = list(filter(lambda i: final[i][0] == team, range(len(final))))[0]
  
  return fstr.format(team, idx+1, suffix(idx+1), points(final[idx]), final[idx][5])

