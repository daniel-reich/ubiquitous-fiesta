
def eval_algebra(eq):
  b=eq.split(" ")
  if b[-1]=="x":return eval("".join(b[0:len(b)-2]))
  else:
    if "+" in b:
      b.remove("x")
      b.remove("+")
      return int(b[-1])-int(b[0])
    else:
      if b[0]=="x":return int(b[2])+int(b[-1])
      else:return int(b[0])-int(b[-1])

