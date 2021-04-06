
def golf_score(course, result):
  score = sum(course)
  result_score = 0
  for i in result: 
    if i == "eagle":
      result_score -= 2
    elif i == "birdie":
      result_score -= 1
    elif i == "par":
      result_score == result_score
    elif i == "bogey":
      result_score += 1
    elif i == "double-bogey":
      result_score += 2
  final_score = score + result_score
  return final_score

