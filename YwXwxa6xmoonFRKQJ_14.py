
def josephus(n):
  n_list     = []
  start_ind  = 0 
  ind_remove = 0 
  if n == 0:
    return False
  for i in range (n):
    n_list.append (i)
  while len (n_list) != 1:
    ind_remove = start_ind + 1
    if ind_remove >= len (n_list):
      ind_remove = ind_remove % (len (n_list))
    n_list.remove ( n_list [ind_remove])
    start_ind = ind_remove
 
  return int (n_list[0])

