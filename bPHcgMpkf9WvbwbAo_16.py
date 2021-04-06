
def format_phone_number(lst):
  lst = ''.join(map(str,lst))
  return '({}) {}-{}'.format(lst[:3],lst[3:6],lst[-4:])

