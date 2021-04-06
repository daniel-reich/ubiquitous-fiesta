
def mathematical(exp, numbers):
  ret = []
  body = exp[5:]
  
  for n in numbers:
    result = int(eval(body.replace(exp[2], str(n)).replace('^', "**").replace('x', '*')))
    ret.append("{}={}".format(exp[:4].replace(exp[2], str(n)), result))
    
  return(ret)

