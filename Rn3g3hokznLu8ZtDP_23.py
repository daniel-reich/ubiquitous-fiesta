
def increment_string(txt):
  if txt[-1].isdigit():
    str_alpha = ''.join([x for x in txt if not x.isdigit()])
    str_num = str(int(txt[-(len(txt)-len(str_alpha)):]) + 1)
    while len(txt)-len(str_alpha)-len(str_num):
      str_num = '0' + str_num
    return str_alpha + str_num
  else:
    return txt + '1'

