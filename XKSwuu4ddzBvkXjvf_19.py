
import re
def prime(n):
  if n == 1: return False
  x = 2
  while x<n:
    if n%x==0: return False
    else: x += 1
  return True
​
def sentence_primeness(sen):
  alph = '0abcdefghijklmnopqrstuvwxyz'
  lst = re.sub(r'[^a-zA-Z 1-9]','', sen).split()
  c = [(w, sum([int(d) for d in w])) if w.isdigit() else (w, sum([alph.index(l.lower()) for l in w])) for w in lst]
  s = sum([x[1] for x in c])
  if prime(s):
    return "Prime Sentence"
  for x,y in c: 
      if prime(s-y):
        return "Almost Prime Sentence ({})".format(x)
  return "Composite Sentence"

