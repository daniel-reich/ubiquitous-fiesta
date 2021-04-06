
import math
​
def group(lst, size):
  groupnum = math.ceil(len(lst) / size)
  groups = []
  for i in range(groupnum):
    groups.append([])
    for j in range(i, len(lst), groupnum):
      groups[i].append(lst[j])
  return groups

