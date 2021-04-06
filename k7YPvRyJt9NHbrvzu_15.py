
def football(score):
  return sum(1 for a in range(score//2+1) for b in range(score//3+1) for c in range(score//6+1) for d in range(score//7+1) for e in range(score//8+1) if 2*a + 3*b + 6*c + 7*d + 8*e == score)

