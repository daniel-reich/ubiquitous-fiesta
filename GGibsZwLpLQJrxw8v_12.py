
def get_lucky_number(size, nth):
  lst = [i for i in range(1, size + 1)]
  z = 1
  eliminate = lst[z]
  l = []
  while len(lst) >= eliminate:
    temp = 1 
    temp_lst = [] 
    for i in range(len(lst)):
      if not temp % eliminate:
        pass
      else:
        temp_lst.append(lst[i])
      temp += 1
    l.append(lst[z])
    lst = temp_lst
    if lst[z] not in l:
      pass
    else:
      z += 1
    eliminate = lst[z]
  return(lst[nth - 1])

