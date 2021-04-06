
def format_phone_number(lst):  
  str_num = ''.join(str(n) for n in lst)
  return "({}) {}-{}".format(str_num[:3], str_num[3:6], str_num[6:])

