
def ping_pong(lst, win):
  k = []
  for index in lst:
    k.append(index)
    k.append("Pong!")
  if win:
    return k
  else:
    return k[:-1]

