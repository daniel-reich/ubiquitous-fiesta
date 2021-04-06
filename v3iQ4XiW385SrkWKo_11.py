
import itertools
def final_result(lst):
  txt = ''.join(lst)
  groups = [''.join(list(g)) for k, g in itertools.groupby(txt)]
​
  ndx = None
  for i in range(len(groups)):
    if len(groups[i]) > 1:
      ndx = i
      break
​
  try:
    groups.pop(ndx)
  except:
    return [i for item in groups for i in item]
​
  return final_result([i for item in groups for i in item])

