
def golf_score(course, result):
  k=0;score=0
  s=('eagle','birdie','par','bogey','double-bogey')
  for i in result:
    score+=course[k]+s.index(i)-2
    k+=1
  return score

