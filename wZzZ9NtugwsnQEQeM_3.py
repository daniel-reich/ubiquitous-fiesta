
def golf_score(course, result):
  d = {"eagle":-2,"birdie":-1,"bogey":1,"double-bogey":2, "par":0}
  s = 0
  for i in range(len(course)):
    s = s + course[i] + d[result[i]]
  return s

