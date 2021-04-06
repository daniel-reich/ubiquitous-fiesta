
def root_digit(n):
  while 1:
    if len(str(n))!=1: n=sum(int(i) for i in str(n))
    else: return n

