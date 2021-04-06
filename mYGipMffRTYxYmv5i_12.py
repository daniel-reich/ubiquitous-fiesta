
def simple_equation(a, b, c):
  a,b = map(str,[a,b])
  for op in "+-*/":
    if eval(a+op+b)==c: return a+op+b+"="+str(c)
  return ""

