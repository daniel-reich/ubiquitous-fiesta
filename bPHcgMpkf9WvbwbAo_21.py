
def format_phone_number(lst):
  lst=''.join([str(x) for x in lst])
  return '({}) {}-{}'.format(lst[:3],lst[3:6],lst[6:])

