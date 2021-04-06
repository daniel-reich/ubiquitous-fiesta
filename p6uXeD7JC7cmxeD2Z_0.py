
def calculate_score(games):
  w = {'R': 'S', 'S': 'P', 'P': 'R'}
  a, b = 0, 0
  for i in games:
    if w[i[0]] == i[1]: a += 1
    elif w[i[1]] == i[0]: b += 1
  return 'Abigail' if a > b else 'Benson' if a < b else 'Tie'

