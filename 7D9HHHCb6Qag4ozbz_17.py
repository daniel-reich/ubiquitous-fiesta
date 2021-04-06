
def find_zip(txt):
  for i in txt:
    if txt.count('zip')>=1:
      return txt.find('zip',txt.find('zip')+1)
  else:
    return -1

