
from fractions import gcd
def ecg_seq_index(n):
  unused = [i for i in range(3, 14 * n)]
  last, lix = 2, 1
  while True:
    for sx in range(len(unused)):
      if gcd(unused[sx], last) > 1:
        lix += 1
        last = unused[sx]
        if last == n:
          return lix
        unused.pop(sx)
        break

