
def fibonacci_sequence():
  a,b=0,1
  f=[a]
  while(b<256):
    f.append(b)
    a,b=b,a+b   
  return f

