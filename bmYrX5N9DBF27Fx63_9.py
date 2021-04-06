
def greatest_impact(x):
  for i in x: i[2] = i[2]*10/3
  y = [sum(abs(x[i][j] - x[i][0]) for i in range(len(x))) for j in range(1, 4)]
  if len(set(y)) < 3: return 'Nothing'  
  if y.index(min(y)) == 0: return 'Weather'
  if y.index(min(y)) == 1: return 'Meals'
  if y.index(min(y)) == 2: return 'Sleep'

