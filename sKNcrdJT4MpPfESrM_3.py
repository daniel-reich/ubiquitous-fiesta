
def remove_virus(files):
  files=files.split('PC Files: ')[1].split(', ')
  ret = []
  for i in files:
    if 'antivirus' in i or 'notvirus' in i:
      ret.append(i)
    elif 'virus' not in i and 'malware' not in i:
      ret.append(i)
  return 'PC Files: '+', '.join(ret) if ret else 'PC Files: Empty'

