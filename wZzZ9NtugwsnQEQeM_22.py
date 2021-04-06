
def golf_score(course, result):
  score = {"eagle":-2, "birdie":-1, "par":0, "bogey":1, "double-bogey":2}
  return sum(score[s] for s in result)+sum(course)

