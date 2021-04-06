
def calculate_score(games):
  res = [0,1,-1]
  score = {'R':1,'P':2,'S':3}
  tot = sum(res[score[a]-score[b]] for a,b in games)
  return 'Abigail' if tot > 0 else 'Benson' if tot < 0 else 'Tie'

