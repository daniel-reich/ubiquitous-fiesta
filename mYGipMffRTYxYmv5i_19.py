
def simple_equation(a, b, c):
  if (a+b == c):
    return "{}+{}={}".format(a,b,c)
  if (a-b == c):
    return "{}-{}={}".format(a,b,c)
  elif(b-a == c):
    return "{}-{}={}".format(b,a,c)
  elif(b*a == c):
    return "{}*{}={}".format(a,b,c)
  elif(b/a == c):
    return "{}/{}={}".format(b,a,c)
  elif(a/b == c):
    return "{}/{}={}".format(a,b,c)
  else:
    return ""

