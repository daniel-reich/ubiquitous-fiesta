
def check_score(s):
  myDict = {'#':5,'O':3,'X':1,'!':-1,'!!':-3,'!!!':-5}
  myScore = 0
  for a in range(len(s)):
    for b in range(len(s[a])):
      myScore += myDict[s[a][b]]
  if myScore < 0:
    return 0
  return myScore

