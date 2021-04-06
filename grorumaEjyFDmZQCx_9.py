
import copy
def is_wristband(lst):
  # horizontal pattern
  for i in range(len(lst)):
    if lst[i].count(lst[i][0]) != len(lst[i]):
      break
  else:
    return True
    
  # vertical pattern
  tmp = copy.deepcopy(lst)
  tmp = ([list(i) for i in zip(*tmp)])
  for i in range(len(tmp)):
    if tmp[i].count(tmp[i][0]) != len(tmp[i]):
      break
  else:
    return True
    
  # diagonal \\ pattern
  n = 0
  tmp = copy.deepcopy(lst)
  tmp[0][len(tmp[0]) - 1] = tmp[len(tmp) - 1] [0] = None
  for i in range(len(tmp)):
    tmp[i] = tmp[i][n:] + tmp[i][:n]
    n += 1
    if n == len(tmp):
      n = 0
  tmp = ([list(i) for i in zip(*tmp)])
  for i in range(len(tmp)):
    tmp[i] = list(filter(None, tmp[i]))
  for i in range(len(tmp)):
    if len(tmp[i]) == 4 and tmp[i][0] == tmp[i][1] and tmp[i][2] == tmp[i][3]:
      continue
    elif tmp[i].count(tmp[i][0]) != len(tmp[i]):
      break
  else:
    return True
    
  # diagonal // pattern
  n = 0
  tmp = copy.deepcopy(lst)
  tmp[0][0] = tmp[len(tmp) - 1] [len(tmp[0]) - 1] = None
  for i in range(len(tmp)):
    tmp[i] = tmp[i][-n:] + tmp[i][:-n]
    n += 1
    if n == len(tmp):
      n = 0
  tmp = ([list(i) for i in zip(*tmp)])
  for i in range(len(tmp)):
    tmp[i] = list(filter(None, tmp[i]))
  for i in range(len(tmp)):
    if len(tmp[i]) == 4 and tmp[i][0] == tmp[i][1] and tmp[i][2] == tmp[i][3]:
      continue
    elif tmp[i].count(tmp[i][0]) != len(tmp[i]):
      break
  else:
    return True
    
  return False

