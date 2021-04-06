
def shift_left(x,y):
  f=lambda a,b:a if b==1else a+f(a,b-1)
  return f(x,2**y)

