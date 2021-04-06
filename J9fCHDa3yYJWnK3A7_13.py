
def is_happy(n):
  if len(str(n))==1:
    return n==1
  else:
    return is_happy(sum(int(x)**2 for x in str(n)))

