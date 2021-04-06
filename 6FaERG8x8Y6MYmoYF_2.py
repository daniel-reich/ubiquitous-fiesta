
def dice_score(throw):
  score = 0
  for i in set(throw):
    if i == 1 and throw.count(1) < 3:
      score += 100
    if i == 5 and throw.count(5) < 3:
      score += 50
    if i == 1 and throw.count(1) >= 3:
      score += 1000
    if i > 1 and throw.count(i) >= 3:
      score += 100 * i
  return score

