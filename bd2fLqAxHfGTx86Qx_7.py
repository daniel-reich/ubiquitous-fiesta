
from re import findall
​
def can_complete(initial, word):
  l_set = '[' + initial + ']'
  init_split = [char for char in initial]
  match = findall(l_set, word)
  
  index = 0
  for i in range(len(init_split)):
    if init_split[i] in match[index:]:
      for j in range(index, len(match)):
        if init_split[i] == match[j]:
          index = j + 1
          break
    else:
      return False
  return True

