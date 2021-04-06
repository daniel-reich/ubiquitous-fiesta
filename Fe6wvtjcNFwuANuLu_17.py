
def ping_pong(lst, win):
  l=[]
  if win:
    for i in range(len(lst)):
      l.append("Ping!")
      l.append("Pong!")
    return l
  else:
    for i in range(len(lst)):
      l.append("Ping!")
      l.append("Pong!")
    l.pop(-1)
    return l

