
def keys_and_values(d):
  re = []
  re.append([])
  re.append([])
  for i in sorted(d):
    re[0].append(i)
    re[1].append(d[i])
  return re

