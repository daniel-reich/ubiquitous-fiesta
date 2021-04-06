
def summation(exp, n):
  return round(sum([eval(exp.replace("n",str(i))) for i in range(1,n+1)]),1)

