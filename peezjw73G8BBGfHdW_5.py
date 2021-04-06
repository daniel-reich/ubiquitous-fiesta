
def arithmetic_operation(n):
  l = n.split()
  f,m,e = int(l[0]),l[1],int(l[2])
  if m == "+":
    return f+e
  elif m == "-":
    return f-e
  elif m == "*":
    return f*e
  elif m == "//" and e != 0:
    return int (f/e)
  else:
    return -1

