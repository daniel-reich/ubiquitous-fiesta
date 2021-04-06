
def remove_virus(files):
  files = files.split(": ")[1].split(", ")
  safe = []
  for i in range(len(files)):
    false_alarm = "antivirus" in files[i] or "notvirus" in files[i]
    if "virus" not in files[i] and "malware" not in files[i] or false_alarm:
      safe.append(files[i])
  if len(safe)==0:
    safe.append("Empty")
  return "PC Files: " + ", ".join(safe)

