
def partition(txt, n):
  rv = []
  for i in range(0, len(txt), n):
    rv.append(txt[i:i+n]) if i+n <= len(txt)-1 else rv.append(txt[i:])
  
  return rv

