
def remove_virus(files):
  lst = files[10:].split(", ")
  new = []
  for i in lst:
    if i == "notvirus.exe" or i == "antivirus.exe":
      new.append(i)
      continue
    if "virus" in i or "malware" in i:
      continue
    new.append(i)
  if len(new) < 1:
    new.append("Empty")
  return files[:10] + ", ".join(new)

