
def cap_to_front(s):
  str1 = ""
  str2 = ""
  for x in s:
    if x.isupper():
      str1 += x
    else:
      str2 += x
  return str1 + str2

