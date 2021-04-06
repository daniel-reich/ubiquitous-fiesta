
def find_zip(txt):
  return txt.find('zip',txt.find('zip')+1) if 'zip' in txt else -1

