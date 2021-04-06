
def recup_factorial(L):
  P = list()
  for elt in L:
    P.append(int(elt[:-1]))
  return P
​
def factorial(n):
  S = 1
  for i in range(1,n+1):
    S *=i
  return S
​
​
def eval_factorial(L):
  S = 0
  P = recup_factorial(L)
  for elt in P:
    S += factorial(elt)
  return S

