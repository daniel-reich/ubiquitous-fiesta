
def format_phone_number(lst):
  lst = ''.join([str(i) for i in lst])
  return '({}) {}-{}'.format(lst[0:3], lst[3:6], lst[6:10])

