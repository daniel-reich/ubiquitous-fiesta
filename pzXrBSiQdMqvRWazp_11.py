
def score_calculator(easy, med, hard):
  score = 0
  score = easy*5 + med*10 + hard*20
  if (easy < 0 or med < 0 or hard < 0):
    score = "invalid"
  return score

