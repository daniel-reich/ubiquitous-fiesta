
def calculate_score(games):
  Abi, Ben = 0, 0
  for i in games:
    if i[0]==i[1]: continue
    if (i[0]=='R' and i[1]=='S') or (i[0]=='P' and i[1]=='R') or (i[0]=='S' and i[1]=='P'):
      Abi += 1
    else:
      Ben += 1
      
  if Abi == Ben:
    return 'Tie'
  elif Abi > Ben:
    return "Abigail"
  else:
    return "Benson"

