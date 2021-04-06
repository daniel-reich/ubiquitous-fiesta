
def check_score(s):
  dic = {'#':5, 'O':3, 'X':1, '!':-1, '!!':-3, '!!!':-5}
  value = sum(dic[sym] for lst in s for sym in lst)
  if value < 0:
    return 0
  return value

