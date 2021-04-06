
def remove_special_characters(txt):
  import re
  p = re.compile(r'[^\w\-\s]')
  return p.sub('', txt)

