
S = {"#":5, "O":3, "X":1, "!":-1, "!!":-3, "!!!":-5}
​
def check_score(s):
  return max([sum(S[j] for i in s for j in i), 0])

