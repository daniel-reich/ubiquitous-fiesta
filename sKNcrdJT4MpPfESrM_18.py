
def remove_virus(files):
  fileNames = files[10:].split(', ')
  copy = fileNames.copy()
  for file in fileNames:
    if file == 'notvirus.exe' or file == 'antivirus.exe':
      continue
    elif 'virus' in file or 'malware' in file:
      copy.remove(file)
  return 'PC Files: Empty' if copy == [] else 'PC Files: ' + ', '.join(copy)

