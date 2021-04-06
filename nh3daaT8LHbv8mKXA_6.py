
def text_to_num(phone):
  num = ""
  for c in phone:
    if c.isalpha():
      num+=numPicker(c)
    else:
      num+=c
  return num
  
def numPicker(letter):
  if letter in "abcABC":
    return '2'
  elif letter in "defDEF":
    return '3'
  elif letter in "ghiGHI":
    return '4'
  elif letter in "jklJKL":
    return '5'
  elif letter in "mnoMNO":
    return '6'
  elif letter in "pqrsPQRS":
    return '7'
  elif letter in "tuvTUV":
    return '8'
  elif letter in "wxyzWXYZ":
    return '9'

