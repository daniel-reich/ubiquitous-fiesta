
def golf_score(course, result):
  return sum([tar - {"eagle": 2, "birdie": 1, "par": 0, "bogey": -1, "double-bogey": -2}[result[i]] for i, tar in enumerate(course)])

