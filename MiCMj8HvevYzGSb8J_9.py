
def fibo_word(n):
  if n<2:return "invalid"
  x1,x2="b","a"
  w= x1+", "+x2
  for i in range(2,n):
   x1,x2=x2,x2+x1
   w=w+", "+x2
​
  return (w)

