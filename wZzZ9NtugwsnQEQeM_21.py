
def golf_score(course, result):
  dic = {"eagle": -2,"birdie": -1,"bogey": 1,
  "double-bogey": 2,"par": 0}
  
  return sum(map(lambda c,r: c+dic[r], course, result))

