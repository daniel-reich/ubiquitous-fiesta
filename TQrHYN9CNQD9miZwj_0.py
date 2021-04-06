
def fix_import(s):
  return 'from {} import {}'.format(s.split()[-1], s.split()[1])

