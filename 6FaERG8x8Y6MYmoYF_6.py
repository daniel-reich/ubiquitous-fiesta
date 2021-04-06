
def dice_score(throw):
  score = 0
  for i in throw:
    if i == 1: score += 100
    if i == 5: score += 50
  for i in range(1,7):
    if throw.count(i) >= 3:
      if i == 1: score += 700
      elif i == 5: score += 350
      else: score += i*100
  return score

