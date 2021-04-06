
def remove_virus(files):
  f = ', '.join([i for i in files[10:].replace(',', '').split() if 'anti' in i or 'not' in i or 'virus' not in i and 'malware' not in i])
  return 'PC Files: ' + f if f else 'PC Files: Empty'

