
def calculate_score(games):
  results = {'S':'R', 'R':'P', 'P':'S'}
  bencounter = 0
  for game in games:
    if results[game[0]] == game[1]:
      bencounter += 1
    elif results[game[1]] == game[0]:
      bencounter -= 1
  if bencounter > 0:
    return "Benson"
  elif bencounter < 0:
    return "Abigail"
  else:
    return "Tie"

