
def mathematical(exp, n):
  exp = exp.replace('^','**').replace('/','//').replace('x','*').split('=')
  for i in range(len(n)):
    temp = exp[0].split('y')[0]+str(n[i])+')='
    temp+=str(eval(exp[1].replace('y',str(n[i]))))
    n[i]=temp
  return n

