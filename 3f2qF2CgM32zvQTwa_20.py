
def format_math(expr):
  e=expr.split()
  if e[1]=='x':
    e[1]='*'
  expr2=" ".join(e) 
  return "{} = {}".format(expr,int(eval(expr2)))

