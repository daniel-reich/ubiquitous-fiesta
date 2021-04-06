
import re
def to_camel_case(txt):
  if not txt:
    return ''
  words = re.findall(r'[A-Za-z]+', txt)
  if words[0][0] == words[0][0].upper():
    return ''.join([word.capitalize() for word in words])
  else:
    return words[0] + ''.join([word.capitalize() for word in words[1:]])

