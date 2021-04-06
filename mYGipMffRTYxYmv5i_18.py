
def simple_equation(a, b, c):
  if a+b==c: return "{}+{}={}".format(a, b, c)
  elif a+c==b: return "{}+{}={}".format(a, c, b)
  elif b+c==a: return "{}+{}={}".format(b, c, a)
  elif a*b==c: return "{}*{}={}".format(a, b, c)
  elif a*c==b: return "{}*{}={}".format(a, c, b)
  elif b*c==a: return "{}*{}={}".format(b, c, a)
  else: return ""

