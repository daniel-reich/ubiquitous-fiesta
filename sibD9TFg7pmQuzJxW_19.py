
from collections import OrderedDict
def stem_plot(lst):
  lst = sorted(lst)
  stems,leaf,out,tree = [],[],[],OrderedDict()
  for i in lst:
    if (i<10):
      stems.append("0")
      leaf.append(str(i))
    else:
      stems.append(str(i)[:-1])
      leaf.append(str(i)[-1])
  for i in range(len(stems)):
    if stems[i] not in tree:
      tree.update({stems[i]:[leaf[i]]})
    else:
      tree[stems[i]].append(leaf[i])
  for key,value in tree.items():
    out.append(key + " | "+ " ".join(value))
  return out

