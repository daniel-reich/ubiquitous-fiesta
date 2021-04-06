
def possible_path(lst):
  dict_nbo = {
    1:[2],
    2:[1, 'H'],
    'H':[2, 4],
    3:[4],
    4:[3,'H']
  }
  if not lst or len(lst) == 1:
    return True 
  i = 1
  while i < len(lst):
    if lst[i] not in dict_nbo[lst[i-1]]:
      return False
    i +=1
  return True

