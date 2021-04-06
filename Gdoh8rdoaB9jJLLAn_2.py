
def summation(exp, i):
      return round(sum(eval(exp.replace('n',str(x))) for x in range(1,i+1)), 1)

