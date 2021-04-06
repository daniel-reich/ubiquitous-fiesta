
def calculate_score(games):
  ans = []
  for i in games:
    abigail = i[0]
    ben = i[1]
    if (abigail == 'P' and ben == 'R') or (abigail == 'R' and ben == 'S') or(abigail == 'S' and ben == 'P'):
      ans.append('A')
    elif (ben == abigail):
      ans.append('T')
    else:
      ans.append('B')
  
  if ans.count('A') > ans.count('B'):
    return 'Abigail'
  elif ans.count('B') > ans.count('A'):
    return 'Benson'
  else:
    return 'Tie'

