
def fix_import(s):
  res = s.split(' ')
  return '{} {} {} {}'.format(res[2], res[3], res[0], res[1])

