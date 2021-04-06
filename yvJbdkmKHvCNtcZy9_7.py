
def is_disarium(n):
  return sum(int(str(n)[i])**(i+1) for i in range(len(str(n)))) == n

