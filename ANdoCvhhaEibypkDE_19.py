
import math
def closing_in_sum(n):
  n = str(n)
  if int(len(n))%2 == 0:
    gb = [n[i] +n[-i-1] for i in range(int(len(n)/2))]
    return (sum([int(i) for i in gb]))
  else:
    bb = [n[i] +n[-i-1] for i in range(math.floor(int(len(n)/2)))]
    return (sum([int(i) for i in bb])) + int(n[len(n)//2])

