
def score_calculator(easy, med, hard):
  if any(i < 0 for i in (easy, med, hard)):
    return 'invalid'
  return easy*5 + med*10 + hard*20

