
def add_up_to(n):
  if(n==0):
    return 0
  else:
    return n+add_up_to(n-1)

