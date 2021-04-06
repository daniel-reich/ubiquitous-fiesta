
import re
def grouping(w):
  group = {}
  for word in w:
    n = len(re.findall(r'[A-Z]',word))
    if not n in group.keys():
      group[n] = [word]
    else:
      group[n].append(word)
      group[n].sort(key = lambda x: x.lower())
  return group

