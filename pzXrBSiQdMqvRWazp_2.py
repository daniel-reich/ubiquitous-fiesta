
def score_calculator(easy, med, hard):
  if easy < 0 or med < 0 or hard < 0:
    return "invalid"
  else:
    return easy * 5 + med * 10 + hard * 20

