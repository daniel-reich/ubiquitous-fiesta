
def is_happy(n):
  return n==1 or (False if n==4 else is_happy(sum(int(i)**2 for i in str(n))))

