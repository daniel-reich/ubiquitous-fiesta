
import re
​
def to_snake_case(txt):
  upperCase = re.sub(r'[^A-Z]', '', txt)
  if len(upperCase) == 0: return txt
  adjusted = re.sub(r'[A-Z]', '_`', txt)
  adjusted = list(adjusted)
  i = 0
  for count, elem in enumerate(adjusted): 
    if elem == '`':
      adjusted[count] = upperCase[i].lower()
      i += 1
  return "".join(adjusted)
​
def to_camel_case(txt):
  txt = list(txt)
  el = []
  for count, elem in enumerate(txt): 
    if elem == '_': el.append(txt[count] + txt[count + 1])
  if len(el) == 0: return "".join(txt)
  newString = "".join(txt)
  for i in el: 
    newString = re.sub(i, i[1].upper(), newString)
  return newString

