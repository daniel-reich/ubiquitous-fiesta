
def check_score(s):
  pts = {'#':5, 'O':3, 'X':1, '!':-1, '!!':-3, '!!!':-5}
  total = 0
  
  for row in s:
    for el in row:
      total += pts[el]
  return max(total, 0)

