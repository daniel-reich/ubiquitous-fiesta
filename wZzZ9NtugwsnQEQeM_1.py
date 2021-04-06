
def golf_score(course, result):
  s=0
  for i in range(len(course)):
    if result[i]=="eagle":
      s+=course[i]-2
    if result[i]=="birdie":
      s+=course[i]-1
    if result[i]=="bogey":
      s+=course[i]+1
    if result[i]=="double-bogey":
      s+=course[i]+2
    if result[i]=="par":
      s+=course[i]
  return s

