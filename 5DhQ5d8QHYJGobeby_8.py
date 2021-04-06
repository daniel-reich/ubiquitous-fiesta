
from statistics import mean
def hot_brick(t):
  prev = 9 * [10* [25]]
  if t == 0:
    return prev + [10*[90]]
  def value(i,j):
    try:
      return 25 if min(i,j) < 0 else prev[i][j]
    except IndexError:
      return 25 if j == 10 else 90
  def avg(i,j):
    return round(mean([value(a+i,b+j) for a,b in zip([-1,-1,-1,0,0,0,1,1,1],[-1,0,1,-1,0,1,-1,0,1])]))
  for k in range(0,t):
    brick = [[avg(i,j) for j in range(0,10)] for i in range(0,9)]
    prev = brick
  return brick + [10*[90]]

