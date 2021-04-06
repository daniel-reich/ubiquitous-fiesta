
def lengthen(s1, s2):
  n1 = len(s1)
  n2 = len(s2)
  res = ""
  if n1 < n2:
    res = ( (int(n2 / n1) + 1) * s1)[ : n2]
  else:
    res = ( (int(n1 / n2) + 1) * s2)[ : n1]
  return res

