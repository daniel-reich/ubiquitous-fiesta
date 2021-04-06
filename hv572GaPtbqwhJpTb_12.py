
def elasticize(w):
​
  l = len(w)//2
  l = list(range(1,l+(2 if len(w)%2 else 1)))
  l += l[::-1][(1 if len(w)%2 else 0):]
​
  return ''.join(list(map(lambda x: x[0] * x[-1] ,list(zip(w,l)))))

