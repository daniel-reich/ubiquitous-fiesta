
def censor_string(txt, lst, char):
  str_list = txt.split(" ")
  for i in range(len(str_list)):
    if str_list[i] in lst:
      str_list[i] = char*len(str_list[i])
  return ' '.join(str_list)

