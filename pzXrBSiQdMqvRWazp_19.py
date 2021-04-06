
def score_calculator(easy, med, hard):
  if easy < 0 or med < 0 or hard < 0:
    return "invalid"
  sumEasy = easy * 5
  sumMed = med * 10
  sumHard = hard * 20
  sum = sumEasy + sumMed + sumHard
  return sum

