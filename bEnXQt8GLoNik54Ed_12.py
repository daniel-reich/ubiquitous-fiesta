
from collections import Counter
def max_score(s):
  cnt = Counter(s)
  
  score = cnt['1']
  rec = 0
  
  for ch in s[:-1]:
    if ch=='0':
      score+=1
    else:
      score-=1
    rec = max(rec, score)
  
  return rec

