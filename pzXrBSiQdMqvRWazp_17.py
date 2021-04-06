
def score_calculator(easy, med, hard):
  if easy>=0 and med>=0 and hard>=0:
    return ((easy*5)+(med*10)+(hard*20))
  else: return 'invalid'

