
def mathematical(exp, numbers):
  a, b, result = "", "", []
​
  if exp.find('^') != -1:
    b = exp.replace('^', '**')
  elif exp.find('x') != -1:
    b = exp.replace('x', '*')
  else:
    b = exp 
  
  for i in numbers:
    a = b.replace("y", str(i))
    a1 = a[:a.index('=')+1]
    a2 = a[a.index('=')+1:]
    result.append(a1 + str(round(eval(a2)))) 
    
  return result

