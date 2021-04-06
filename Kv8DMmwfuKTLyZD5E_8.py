
from math import ceil
def make_dartboard(n):
  if n == 1: return [1]
  db, c = [], ceil(n/2)
  for i in range(c):
    a = ''.join([str(j+1) for j in range(i)])
    db.append(int(a + str(i+1)*(n - len(a)*2) + a[::-1]))
  return db + db[n//2-1::-1]

