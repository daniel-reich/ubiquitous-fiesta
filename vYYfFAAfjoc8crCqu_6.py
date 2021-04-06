
def tree(h):
  lst = []
  for i in range(0,h):
    lst.append(" "*(h-i-1)+"#"*(1+2*i)+" "*(h-i-1))
  return lst

