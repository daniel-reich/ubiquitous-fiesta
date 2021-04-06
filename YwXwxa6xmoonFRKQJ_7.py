
def josephus(n):
  if n < 1: return False
  circle, k = list(range(n)), 0
  while len([p for p in circle if p != -1]) > 1:
    if circle[k] == -1: k = (k+1)%n
    else: circle[circle.index([x for x in circle[k+1:]+circle[:k] if x!=-1][0])],k = -1,(k+2)%n
  return max(circle)

