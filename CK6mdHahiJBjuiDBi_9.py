
def can_fit(weights, bags):
  w1=sorted(weights)
  A=[]
  B=[]
  while True:
    B.append(w1.pop(0))
    if w1 and sum(B)+w1[-1]<=10:
      B.append(w1.pop())
    if w1 and sum(B)+w1[0]>10:
      A.append(B)
      B=[]
    if not w1:
      A.append(B)
      break
  C=[]
  D=[]
  while True:
    D.append(weights.pop(0))
    if weights and sum(D)+weights[0]>10:
      C.append(D)
      D=[]
    if not weights:
      C.append(D)
      break
  return min(len(A), len(C))<=bags

