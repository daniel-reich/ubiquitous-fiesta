
def square_root(n): #Newton's method
  a = n//2
  while True:
    b = (a+(n//a))//2
    if b >= a:
      return a
    a = b

