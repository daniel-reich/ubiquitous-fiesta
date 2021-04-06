
from string import ascii_lowercase as a, punctuation as p
from itertools import combinations as cb
def sentence_primeness(sentence):
  def ip(n):
    return n==2 or all(n%d for d in range(3,int(n**.5)+1,2)) and bool(n%2) and n>2
​
  s = sentence.translate(str.maketrans("","",p)).split()
  d = {v:k for k,v in enumerate(a,1)}
  d.update({str(x): x for x in range(10)})
  w = [sum(d.get(c) for c in w.lower()) for w in s]
  wc = [ip(sum(x)) for x in cb(reversed(w),len(w)-1)]
  if ip(sum(w)):
    return "Prime Sentence"
  elif any(wc):
    return "Almost Prime Sentence ({})".format(s[wc.index(True)])
  else:
    return "Composite Sentence"

