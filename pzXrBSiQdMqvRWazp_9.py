
def score_calculator(easy, med, hard):
  easy = easy * 5
  med = med * 10
  hard = hard * 20
  return easy + med + hard if easy >=0 and med >= 0 and hard >=0 else 'invalid'

