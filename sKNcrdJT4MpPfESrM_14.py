
def remove_virus(files):
  files = files[10:]
  print(files)
  l = list()
  for elt in files.split(', '):
    if "virus" not in elt and "malware" not in elt:
      l.append(elt)
    if "antivirus" in elt or "notvirus" in elt:
      l.append(elt)
  
  s = 'PC Files: '
  for elt in l:
    s += elt + ", "
    
  if len(l) == 0:
    return s + "Empty"
    
  return s[:-2]

