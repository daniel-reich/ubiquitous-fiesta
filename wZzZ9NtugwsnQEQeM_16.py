
def golf_score(course, result):
  terms = {"eagle": -2, "birdie": -1, "par": 0, "bogey": 1, "double-bogey": 2}
  return sum(c + terms[r] for c, r in zip(course, result))

