
def soroban(m):
  s = 0
  trans = {0 : 5, 1 : 0,2 : 0, 3 : 0, 4 : 1, 5 : 2, 6 : 3, 7 : 4}
​
  for n, row in enumerate([[m[j][i] for j in range(len(m))] for i in range(len(m[0]))][::-1]):
    s += sum([trans[m]*10**n for m, val in enumerate(row) if val=="|"])
  
  return s

