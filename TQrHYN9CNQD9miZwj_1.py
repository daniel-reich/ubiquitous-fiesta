
def fix_import(s):
  return ' '.join(s.split()[-2:] + s.split()[:2])

