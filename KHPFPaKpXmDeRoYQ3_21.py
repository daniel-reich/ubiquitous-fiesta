
def check_score(s):
  matching = {'#':5,'O':3,'X':1,'!':-1,'!!':-3,'!!!':-5}
  ans = 0
  for lst in s:
    for symbol in lst:
      ans += matching[symbol]
  if ans<0:
    return 0
  return ans

