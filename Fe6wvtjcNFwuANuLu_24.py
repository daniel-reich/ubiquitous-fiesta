
def ping_pong(lst, win):
  ret_lst = []
  
  for hit in lst:
    ret_lst.append(hit)
    ret_lst.append("Pong!")
    
  if win:
    return ret_lst
  else:
    return ret_lst[0:-1]

