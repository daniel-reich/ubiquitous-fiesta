
def golf_score(course, result):
  score = []
  golfTerms = ['eagle', 'birdie', 'par', 'bogey', 'double-bogey']
  n = 0
  for i in result:
    scoreAdj = (golfTerms.index(i) - 2)
    score.append(course[n] + scoreAdj)
    n += 1
  return(sum(score))

