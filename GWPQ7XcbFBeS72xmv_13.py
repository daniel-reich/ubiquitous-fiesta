
def calculate_scores(txt):
  a = 0
  b = 0
  c = 0
  for x in txt:
    if x == 'A':
      a += 1
    elif x == 'B':  
      b += 1
    elif x == 'C':  
      c += 1
  score = [a, b, c]
  return score

