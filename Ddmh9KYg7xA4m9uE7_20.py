
def convert_binary(string):
  s=''
  for i in string.lower():
    if ord(i)<110:
      s+='0'
    else:
      s+='1'
  return s

