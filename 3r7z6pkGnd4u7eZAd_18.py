
def mark_maths(l):
  
  t = 0
​
  for exp in l:
    exp = exp.split('=')
    t += 1 if eval(exp[0])==int(exp[-1]) else 0
​
  return str(round( t/len(l)*100 ))+'%'

