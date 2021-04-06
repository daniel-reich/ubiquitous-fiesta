
def get_xp(d):
  score = 0
  d1 = {"Very Easy" : 5, "Easy" : 10, "Medium" : 20, "Hard" : 40, "Very Hard" : 80}
  for i in d:
    score += d[i] * d1[i]
  return str(score) + "XP"

