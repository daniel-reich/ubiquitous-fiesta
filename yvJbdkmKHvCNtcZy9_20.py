
def is_disarium(n):
  return sum(int(d)**(i+1) for i,d in enumerate(str(n))) == n

