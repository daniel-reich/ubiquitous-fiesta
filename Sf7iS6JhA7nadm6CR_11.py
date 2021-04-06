
import itertools
def divisibility_rule(n):
  x = []
  count = 0
  seq = [1, 10, 9, 12, 3, 4]
  y = itertools.cycle(seq)
  for value in y:
    x.append(value)
    count += 1
    if count > len(str(n))-1 :
      break
  nn = str(n)[::-1]
  z = sum([int(nn[i])*x[i] for i in range(len(nn))])
  if n != z:
    n = divisibility_rule(z)
  return n

