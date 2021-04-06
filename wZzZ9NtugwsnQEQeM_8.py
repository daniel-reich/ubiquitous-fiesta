
def golf_score(course, result):
  s = 0
  for i in range(0, len(course)):
    if result[i] == "eagle":
      s += (-2 + course[i])
    elif result[i] == "birdie":
      s += (-1 + course[i])
    elif result[i] == "bogey":
      s += (1 + course[i])
    elif result[i] == "double-bogey":
      s += (2 + course[i])
    else:
      s += course[i]      
  return s

