
from copy import deepcopy
def sortW(scores):
  sList = []
  rest = deepcopy(scores)
  while len(sList) != len(scores):
    winner, rest = winnerByScore(rest)
    sList.append(winner)
  return sList
def winnerByScore(scores):
  max = 0
  if len(scores) == 1:
    return scores[0], []
  for i, score in enumerate(scores):
    if score[1] > scores[max][1]:
      max = i 
  for i, score in enumerate(scores):
    if i != max and score[1] == scores[max][1]:
      win = winnerByGoal(list(filter(lambda x : x[1] == scores[max][1], scores)))
      for i2, score2 in enumerate(scores):
        if score2[0] == win[0]: max = i2
  return scores[max], [scores[n] for n in range(len(scores)) if n != max] 
def winnerByGoal(scores):
  max = 0
  for i, score in enumerate(scores):
    if score[2] > scores[max][2]:
      max = i 
  for i, score in enumerate(scores):
    if i != max and score[2] == scores[max][2]:
      return winnerByDif(list(filter(lambda x: x[2]==scores[max][2], scores)))
  return scores[max]
def winnerByDif(scores):
  max = 0
  for i, score in enumerate(scores):
    if score[3] > scores[max][3]:
      max = i 
  return scores[max]
def tabulate(t1, s1, t2, s2, mem):
  s1, s2 = int(s1), int(s2)
  if s1 == s2:
    p1 = p2 = 1
  elif s1 > s2:
    p1 = 3
    p2 = 0
  else:
    p1 = 0
    p2 = 3  
  if t1 not in mem.keys():
    mem[t1] = (p1, s1, s1-s2)
  else:
    a,b,c = mem[t1]
    mem[t1] = (p1+a, s1+b, s1-s2+c)
  if t2 not in mem.keys():
    mem[t2] = (p2, s2, s2-s1)
  else:
    a,b,c = mem[t2]
    mem[t2] = (p2+a, s2+b, s2-s1+c)   
  return mem
  
  
def tournament_scores(lst):
  mem = {}
  for entry in lst:
    fst, scd = entry.split(" - ")
    t1, s1 = fst.split()
    s2, t2 = scd.split()
    mem = tabulate(t1, s1, t2, s2, mem)
  result = []
  for team in mem.keys():
    a,b,c = mem[team]
    result.append([team, a, b, c])
  return sortW(result)

