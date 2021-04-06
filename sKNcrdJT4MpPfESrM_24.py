
from re import split
def remove_virus(files):
  files=split('[,:]',files)[1:]
  new=[]
  for file in files:
    if 'virus' not in file and 'malware' not in file:
      new.append(file)
    else:
      if 'antivirus'in file or 'notvirus' in file:
        new.append(file)
  if not len(new):
    return 'PC Files: Empty'
  return "PC Files:"+','.join(new)

