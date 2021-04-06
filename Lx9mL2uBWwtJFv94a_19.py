
def checker_board(n, el1, el2):
  if el1 == el2:
    return "invalid"
  
  lst = []
  idx_lst = [el1, el2]
  
  idx = 0
  for i in range(n):
    x = []
    for j in range(n):
        x.append(idx_lst[idx % 2])
        idx += 1
    lst.append(x)
    if n % 2 == 0:
      idx += 1
    
  return lst

