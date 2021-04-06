
def golf_score(course, result):
  res = 0
  dic = {"eagle" : -2, "birdie" : -1, "bogey" : +1 , "double-bogey" : +2, "par" : 0}
  for i in range(0, len(course)):
    res += course[i] + dic[result[i]]
  return res

