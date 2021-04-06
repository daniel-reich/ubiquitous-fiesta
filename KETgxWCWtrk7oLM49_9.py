
def tournament_scores(lst):
  pt = {}
  gs = {}
  gd = {}
  scores = []
  for s in lst:
    split = s.split()
    if split[0] in gs:
      gs[split[0]] += int(split[1])
      gd[split[0]] += (int(split[1]) - int(split[3]))
      if (int(split[1]) - int(split[3])) > 0:
        pt[split[0]] += 3
      if (int(split[1]) - int(split[3])) == 0:
        pt[split[0]] += 1
    else:
      gs[split[0]] = int(split[1])
      gd[split[0]] = (int(split[1]) - int(split[3]))
      if (int(split[1]) - int(split[3])) > 0:
        pt[split[0]] = 3
      elif (int(split[1]) - int(split[3])) == 0:
        pt[split[0]] = 1
      else:
        pt[split[0]] = 0
    if split[-1] in gs:
      gs[split[-1]] += int(split[-2])
      gd[split[-1]] += (int(split[-2]) - int(split[1]))
      if (int(split[-2]) - int(split[1])) > 0:
        pt[split[-1]] += 3
      if (int(split[-2]) - int(split[1])) == 0:
        pt[split[-1]] += 1
    else:
      gs[split[-1]] = int(split[-2])
      gd[split[-1]] = (int(split[-2]) - int(split[1]))
      if (int(split[-2]) - int(split[1])) > 0:
        pt[split[-1]] = 3
      elif (int(split[-2]) - int(split[1])) == 0:
        pt[split[-1]] = 1
      else:
        pt[split[-1]] = 0
  teams = gs.keys()
  for i in teams:
    score = []
    score.append(i)
    score.append(pt[i])
    score.append(gs[i])
    score.append(gd[i])
    scores.append(score)
  return sorted(scores, key=lambda word: (word[1], word[2], word[3]), reverse = True)

