
def ping_pong(lst, win):
  i = 0
  while i < len(lst):
    if lst[i] == "Ping!": lst.insert(i+1,"Pong!")
    i += 1
  if win == False: lst.pop()
  return lst

