
import re
def dakiti(sentence):
  sentence=sentence.strip()
  A=sentence.split()
  B=sorted(A, key=lambda x: int(re.search(r'\d', x).group()))
  res=[]
  for x in B:
    t=''
    for y in x:
      if not y.isdigit():
        t+=y
    res.append(t)
  return ' '.join(res)

