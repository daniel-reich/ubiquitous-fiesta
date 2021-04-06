
def drange(*args):
  lst = []
  if len(args)>1:
    n = args[0]
  else:
    return tuple([i for i in range(args[0])])
  while n < args[1]:
    lst.append(n)
    if len(args)>2:
      n+=args[2]
      n = round(n,3)
    else:
      n+=1
  return tuple(lst)

