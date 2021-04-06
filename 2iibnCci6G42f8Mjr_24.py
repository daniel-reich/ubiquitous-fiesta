
def guess_score(code, guess):
  c1=list(code)
  g1=list(guess)
  t1,t2=0,0
  for i in range(0,4):
    if c1[i]==g1[i]:
      t1+=1
    else:
      if c1[i] in g1:
        t2+=1
  return {"black":t1,"white":t2}

