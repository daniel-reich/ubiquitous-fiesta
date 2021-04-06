
def format_phone_number(lst):
  l = ''.join(map(str, lst))
  return '({}) {}-{}'.format(l[0:3], l[3:6], l[6:])

