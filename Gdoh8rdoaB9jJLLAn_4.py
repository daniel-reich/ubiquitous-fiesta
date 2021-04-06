
def summation(exp, n):
  if exp == '0':
    return 0
  def f(s,n):
    if n == 0:
      return round(s,1)
    return f(s+eval(exp.replace('n',str(n))),n-1)
  return f(0,n)

