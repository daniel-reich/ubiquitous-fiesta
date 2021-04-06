
from itertools import count
def ecg_seq_index(n):
  def pf(num):
    output = set()
    for i in range(2, num//2+1):
      while not num % i:
        output.add(i)
        num //= i
    if num > 1:
      output.add(num)
    return output
​
  seq = [1,2]
  while n not in seq:
    for x in count():
      if x not in seq and (pf(x) & pf(seq[-1])):
        seq.append(x)
        break
  return seq.index(n)

