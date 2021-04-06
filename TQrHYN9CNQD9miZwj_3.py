
def fix_import(s):
  words = s.split()
  return ' '.join(words[2:] + words[:2])

