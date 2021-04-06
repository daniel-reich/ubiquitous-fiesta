
def fix_import(s):
  words = s.split()
  return ' '.join([words[2], words[3], words[0], words[1]])

