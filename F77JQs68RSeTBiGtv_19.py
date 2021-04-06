
from statistics import median
def diamond_sum(n):
  if n == 1:
    return 1
  def center(x):
    start = x*n+1
    end = n*(x+1)
    return median(list(range(start,end+1)))
  nth_term = lambda x: center(x) if x == 0 or x == n-1 else 2 * center(x)
  return sum(list(map(lambda x: nth_term(x),range(0,n))))

