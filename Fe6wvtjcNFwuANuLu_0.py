
def ping_pong(lst, win):
  res = ['Ping!', 'Pong!'] * len(lst)
  return res if win else res[:-1]

