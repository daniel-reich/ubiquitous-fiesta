
def help(lst,pos):
  if len(lst)==1:
#   print("done")
    return(lst[0])
  next=(pos+1)%len(lst)
  print(lst,"remove:",next, lst[next])
  del lst[next]
  return(help(lst,next%len(lst)))
  
​
def josephus(n):
  if n<2:
    return(False)
  print(n)
  return(help([i for i in range(0,n)],0))

