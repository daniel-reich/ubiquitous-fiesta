
def ping_pong(lst, win):
  new_lst = []
  word_lst = ["Ping!", "Pong!"]
  for i in lst[:-1]:
    new_lst.extend(word_lst)
  if win:
      new_lst.extend(word_lst)
  else:
    new_lst.append("Ping!")
  return new_lst

