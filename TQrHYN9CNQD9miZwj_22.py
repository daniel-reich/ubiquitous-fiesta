
def fix_import(s):
  l = s.split()
  return ' '.join(l[-2:]+ l[0:2])

