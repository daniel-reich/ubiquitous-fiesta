
def binary_conversion(txt):
  import re
  chars=re.findall('.{1,8}',txt)
  str=[chr(int(letter,2)) for letter in chars]
  return (''.join(str))

