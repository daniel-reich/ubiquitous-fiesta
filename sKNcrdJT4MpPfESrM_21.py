
def remove_virus(files):
  files = files[10:].split(", ")
  to_remove = []
  for _, file in enumerate(files):
    if "malware" in file or ("virus" in file and "antivirus" not in file and "notvirus" not in file):
      to_remove.append(file)
  for file in to_remove:
    files.remove(file)
  if files == []:
    files = "PC Files: " + "Empty"
  else:
    files = "PC Files: " + ", ".join(files)
  return files

