
def is_disarium(N):
  return sum(int(n)**(i+1) for i, n in enumerate(str(N))) == N

