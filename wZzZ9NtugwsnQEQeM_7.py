
def golf_score(course, result):
  score=0
  for i in range(len(course)):
    if result[i]=='eagle':
      score+=course[i]-2
    elif result[i]=='birdie':
      score+=course[i]-1
    elif result[i]=='bogey':
      score+=course[i]+1
    elif result[i]=='par':
      score+=course[i]
    elif result[i]=='double-bogey':
      score+=course[i]+2
  return score

