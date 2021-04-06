
def check_score(s):
  symbols = {'#':5,'O':3,'X':1,'!':-1,'!!':-3,'!!!':-5}
  total = sum(symbols[j] for i in s for j in i)
  return total if total>0 else 0

