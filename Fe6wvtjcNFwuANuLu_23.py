
def ping_pong(lst, win):
  if win:
    lst = ' Pong! '.join(lst)
    lst = lst.split(' ')
    lst.append('Pong!')
    return lst
  else:
    lst = ' Pong! '.join(lst)
    lst = lst.split(' ')
    return lst

