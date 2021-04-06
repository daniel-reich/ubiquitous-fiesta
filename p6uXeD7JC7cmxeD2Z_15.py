
def calculate_score(games):
  mat = [
    [0,-1,1],
    [1,0,-1],
    [-1,1,0]
  ]
  myDict = {
    'R':0,
    'P':1,
    'S':2
  }
  sum = 0
  for game in games:
    sum += mat[myDict[game[0]]][myDict[game[1]]]
  if sum > 0:
    return 'Abigail'
  elif sum < 0:
    return 'Benson'
  else:
    return 'Tie'

