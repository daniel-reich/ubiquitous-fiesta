
def check_score(s):
  dic = {"#":5, "O":3, "X":1, "!":-1, "!!":-3, "!!!":-5}
  s = sum(s, [])
  return max(0,sum(dic[i]*s.count(i) for i in set(s)))

