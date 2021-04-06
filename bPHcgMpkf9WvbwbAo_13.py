
def format_phone_number(lst):
  lst1 = [str(i) for i in lst]
  a = ''.join(lst1)
  return '({}) {}-{}'.format(''.join(lst1[:3]), ''.join(lst1[3:6]), ''.join(lst1[6:]))

