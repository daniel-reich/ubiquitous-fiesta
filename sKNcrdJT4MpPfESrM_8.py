
import re
​
def remove_virus(files):
  finalList = []
  for i in re.split(r':\s', files)[1].split(", "):
    if re.search(r'\w+virus', i):
      if re.search(r'antivirus', i):
        finalList.append(i)
      elif re.search(r'notvirus', i):
        finalList.append(i)
    else:
      if re.search(r'^virus', i):
        continue
      if not re.search(r'malware', i):
        if not re.search(r'\w+malware', i):
          finalList.append(i)
  return "PC Files: " + ", ".join(finalList) if finalList else "PC Files: Empty"

