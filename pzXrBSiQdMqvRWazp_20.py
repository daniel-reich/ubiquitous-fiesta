
def score_calculator(easy, med, hard):
  return "invalid" if len([1 for i in [easy,med,hard] if i<0])>0 else easy*5+med*10+hard*20

