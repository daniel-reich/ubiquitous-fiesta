
def freq_count(lst, el, s = [], level = 0):
  if level == 0:
    s = []
  if len(s) <= level:
    s.append([level, 0])
  s[level][1] += lst.count(el)
  for x in lst:
    if isinstance(x, list):
      freq_count(x, el, s, level + 1)
  return s

