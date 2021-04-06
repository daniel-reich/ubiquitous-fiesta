
def truncate(txt, length):
  if length>len(txt): return txt
  if txt[length]==' ': return txt[:length]
  ind=0
  for i in range(length):
    if txt[i]==' ': ind=i
  return txt[:ind]

