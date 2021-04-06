
def arithmetic_operation(n):
  a , b, c = n.split()
  if b == "//": return -1 if c=='0' else  int(a)//int(c)
  elif b == "+": return int(a) + int(c)
  elif b == "-": return int(a) - int(c)
  else: return int(a) * int(c)

