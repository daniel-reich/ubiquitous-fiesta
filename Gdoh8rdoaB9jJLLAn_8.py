
def summation(exp, n):
  return round(sum([eval(exp.replace("n","x")) for x in range(1,n+1) ]),1)

