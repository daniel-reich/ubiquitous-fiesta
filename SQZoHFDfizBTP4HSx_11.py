
from collections import Counter
def missing_alphabets(txt):
  d=Counter(txt)
  m=max(d[x] for x in d)
  alphas='abcdefghijklmnopqrstuvwxyz'
  miss=''
  for alph in alphas:
    if alph in d:
      miss+=alph*(m-d[alph])
    else:
      miss+=alph*m
  return miss

