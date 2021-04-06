
def truncate(s, ln):
  if ln > len(s):
    return s
  words = s.split()
  if ln < len(s) // 2 and not len(words) % 2:
    return ""
  middle = words[len(words) // 2]
  res = s[:ln]
  res2 = res.split() 
  l = ' '.join([word for word in res2 if word not in middle])
  return l

