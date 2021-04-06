
def format_num(n):
  lst = list(str(n))
  lst.reverse()
  l = []
  for i in range(0,len(lst)):
    if i in range(3,len(lst),3):
      l.append(lst[i]+",")
    else:
      l.append(lst[i])
  
  l.reverse()  
  return "".join(l)

