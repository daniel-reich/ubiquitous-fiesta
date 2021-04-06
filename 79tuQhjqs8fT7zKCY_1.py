
def postfix(expr):
  lst=expr.split()
  res=lst.pop(0)
  while lst:
    if lst[1].isdigit():
      lst[0] = str(eval('{}{}{}'.format(lst[0],lst.pop(2),lst.pop(1))))
    else:
      res = eval('{}{}{}'.format(res,lst.pop(1),lst.pop(0)))
  return int(res)

