
def score_calculator(easy, med, hard):
  return 'invalid' if any([i<0 for i in [easy,med,hard]]) else (5*easy)+(10*med)+(20*hard)

