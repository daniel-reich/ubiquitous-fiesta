
import re
def color_conversion(h):
  if isinstance(h,dict):
    if any(list(map(lambda x: x > 255 or x < 0, h.values()))):
      return "Invalid input!"
    string = ''.join('{:02X}'.format(a) for a in [h['r'],h['g'],h['b']])
    return "#" + string.lower()
  elif bool(re.search(r'[^f]+ff|ff[^f]',h)) == True:
    return "Invalid input!"
  else:
    dictionary = {}
    h = h.lstrip("#")
    for char,letter in zip([h[x:x+2] for x in range(0,6,2)],['r','g','b']):
      dictionary[letter] = int(char,16)
    return dictionary

