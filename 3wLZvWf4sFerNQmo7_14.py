
def neutralise(s1, s2):
  res_str = ""
  for str1,str2 in zip(s1,s2):
    if str1 == str2:
      res_str += str1
    else:
      res_str += "0"
  return res_str

