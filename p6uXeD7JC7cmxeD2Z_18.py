
import numpy as np
def calculate_score(games):
  res = np.array([[0,2,1],[1,0,2],[2,1,0]])
  choice = {"R":0,"P":1,"S":2}
  res2 = {0:"T",1:"A",2:"B"}
  counts = [0,0]
  for game in games:
    temp = res2[res[choice[game[0]]][choice[game[1]]]]
    if temp == "T":
      continue
    elif temp == "A":
      counts[0] += 1
    elif temp == "B":
      counts[1] += 1
  if counts[0] == counts[1]:
    return 'Tie'
  elif counts[0] > counts[1]:
    return "Abigail"
  else:
    return "Benson"

