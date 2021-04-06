
def summation(exp, n):
  e = exp.replace("n","{0}")
  return round(sum(eval(e.format(i)) for i in range(1,n+1)),1)

