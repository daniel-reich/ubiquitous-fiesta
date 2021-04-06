
def cardi(n):
  return str(n) + {1: 'st', 2: 'nd', 3: 'rd'}.get(n, 'th')
​
​
def EPLResult(teams, obj):
  stand = sorted(teams, key=lambda x: (x[2] * 3 + x[3], x[-1]), reverse=True)
  stand = [i + 1 for i in range(len(stand)) if stand[i][0] == obj][0]
  points = [(t[2] * 3) + t[3] for t in teams if t[0] == obj][0]
  goal_diff = [t[5] for t in teams if t[0] == obj][0]
  res = "{} came {} with {} points and a goal difference of {}!"
​
  return res.format(obj, cardi(stand), points, goal_diff)

