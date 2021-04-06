
def award_prizes(names):
  names1 = {v:k for k, v in names.items()}
  u = sorted(names1.keys())[::-1]
  y = {}
  for i in range(len(u)):
    if i == 0:
      y[names1[u[i]]] = 'Gold'
    elif i == 1:
      y[names1[u[i]]] = 'Silver'
    elif i == 2:
      y[names1[u[i]]] = 'Bronze'
    else:
      y[names1[u[i]]] = 'Participation'
  return y

