
def golf_score(course, result):
  terms = ['eagle', 'birdie', 'par', 'bogey', 'double-bogey']
  return sum([course[i]+terms.index(result[i])-2 for i in range(18)])

