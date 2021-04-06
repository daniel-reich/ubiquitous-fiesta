
def score_calculator(easy, med, hard):
  return 'invalid' if easy<0 or med<0 or hard<0 else easy*5+med*10+hard*20

