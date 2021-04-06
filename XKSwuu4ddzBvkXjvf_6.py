
import string
import re
def sentence_primeness(strings):
  lst = {x: y for x,y in zip(string.ascii_lowercase, range(1, 27))}
  lst.update({x: y for x,y in zip(string.ascii_uppercase, range(1, 27))})
  lm = strings.split()
  totalnum, total = 0, 0
  lstnum = {}
  for o in lm:
    total = 0
    for j in o:
      total = total + (lst.get(j) if j.isalpha() else (int(j) if j.isnumeric() else 0))
    totalnum = totalnum + total
    lstnum.update({o: str(total)})
  if isprime(totalnum): 
    return "Prime Sentence" 
  else:
    for j in lstnum:
      if isprime(totalnum - int(lstnum.get(j))):
        return "Almost Prime Sentence (" + re.sub(r"[^a-zA-Z0-9]+", '', j) + ")"
    return "Composite Sentence"
​
def isprime(num):
  if num > 1:
    for i in range(2,num//2):
      if num%i == 0:
        return False
    else:
      return True
  else:
    return False

