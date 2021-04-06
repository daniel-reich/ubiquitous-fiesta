
def elasticize(word):
  fin = ''
  if len(word) % 2 == 1:
    mults = [a+1 for a in list(range(len(word)//2))+list(range(len(word)//2,-1,-1))]
  else:
    mults = [a+1 for a in list(range(len(word)//2))] + sorted([a+1 for a in list(range(len(word)//2))],reverse=True)
  for a,b in zip(word,mults):
    fin += a*b
  return fin

