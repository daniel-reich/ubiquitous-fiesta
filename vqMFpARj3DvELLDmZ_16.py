
def letters_only(txt):
  import re
  return ''.join(re.findall('[a-zA-Z]',txt))

