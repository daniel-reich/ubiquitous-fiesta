
def golf_score(course, result):
  golf = {"eagle":-2, "birdie":-1, "par":0, "bogey":1, "double-bogey":2}
  return sum(golf[result[i]]+course[i] for i in range(len(result)))

