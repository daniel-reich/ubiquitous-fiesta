
def guess_score(code, guess):
  A=[]
  B=[]
  for i, n in enumerate(code):
    if n==guess[i]:
      A.append(n)
      guess.replace(guess[i], '')
    else:
      B.append(n)
  c=0
  for x in B:
    if x in guess:
      c+=1
  return {"black": len(A), "white": c}

