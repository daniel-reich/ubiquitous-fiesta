
def boxes(w):
​
  b,n = 0,0
​
  for i in range(len(w)+1):
    if sum(w[n:i+1]) > 10:
      b += 1
      n = i
​
  return b + ( 1 if n != i else 0 )

