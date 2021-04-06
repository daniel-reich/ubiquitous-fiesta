
def pingPong(lst, win):
  l = []
  for i in range(len(lst) - 1):
    l.extend(['Ping!', 'Pong!'])
  return l + ['Ping!'] + ['Pong!'] * win

