
def remove_virus(files):
  f = files[10::].split(', ')
  r = []
  for file in f:
    v = False
    if ("virus" in file and not "notvirus" in file and not "antivirus" in file) or "malware" in file:
      v = True
    if not v:
      r.append(file)
  if len(r) > 0:
    return "PC Files: " + ", ".join(r)
  else:
    return "PC Files: Empty"

