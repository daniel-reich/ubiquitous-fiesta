
def ping_pong(lst, win):
  i = 0
  orgLen = len(lst)
  while(i < orgLen*2):
    if lst[i] == 'Ping!':
      lst.insert(i+1, 'Pong!')
    i += 1
  if win == False:
    del lst[-1]
  return lst

