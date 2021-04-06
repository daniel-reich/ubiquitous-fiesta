
def ping_pong(lst, win):
  for i in range(1, len(lst)*2, 2):
    lst.insert(i, 'Pong!')
  return lst if win else lst[:-1]

