
def max_possible(n1, n2):
  x = sorted(list(i for i in str(n2)))
  y = list(i for i in str(n1))
  for i in range(len(y)):
     if int(y[i])<int(x[-1]):
        y[i]=str(x[-1]);x = x[:-1]
        if len(x)==0:return int("".join(y)) 
  return int("".join(y))

