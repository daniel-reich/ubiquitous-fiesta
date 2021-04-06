
def is_disarium(n):
  return True if n==sum([int(str(n)[i-1])**(i) for i in range(1,len(str(n))+1) ]) else False

