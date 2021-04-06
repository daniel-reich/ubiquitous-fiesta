
def format_math(expr):
  lst=list(expr.split())
  if lst[1]=="+":
    res=int(lst[0])+ int(lst[2])
  elif lst[1]=="-":
    res=int(lst[0])- int(lst[2])
  elif lst[1]=="x":
    res=int(lst[0])* int(lst[2])
  elif lst[1]=="/":
    res=int(int(lst[0])/ int(lst[2]))
  return"{}{}{}".format(expr," = ",res)

