
def collect(s, n):
  newlist = []
  for i in range(0,len(s),n):
    if len(s[i:i+n]) != n:
      continue
    else:
      newlist.append(s[i:i+n])
  return sorted(newlist)

