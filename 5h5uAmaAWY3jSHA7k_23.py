
def landscape_type(lst):
  if sorted(lst) == lst or sorted(lst, reverse= True) == lst:
    return 'neither'
  reached = False
  mountain = True
  for a in range(len(lst) - 1):
    if lst[a] > lst[a + 1]:
      mountain = False
      break
    elif lst[a] < lst[a + 1]:
      break
  if mountain:
    if lst.count(max(lst)) > 1:
      return 'neither'
  else:
    if lst.count(min(lst)) > 1:
      return 'neither'
  for a in range(len(lst) - 1):
    if (reached and mountain and lst[a] < lst[a + 1]) or (reached and not mountain and lst[a] > lst[a + 1]):
      return 'neither'
    if (not mountain and lst[a] == min(lst)) or (mountain and lst[a] == max(lst)) :
      reached = True
    if (not reached and not mountain and lst[a] < lst[a + 1]) or (not reached and mountain and lst[a] > lst[a + 1]):
      return 'neither'
  if mountain:
    return 'mountain'
  else:
    return 'valley'

