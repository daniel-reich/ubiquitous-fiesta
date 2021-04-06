
def format_phone_number(lst):
  str_lst = ''.join([str(c) for c in lst])
  return "({0}) {1}-{2}".format(str_lst[:3], str_lst[3:6], str_lst[6:])

