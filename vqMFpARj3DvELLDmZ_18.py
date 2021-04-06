
def letters_only(txt):
  import re
  return ''.join(re.findall('[A-Za-z]',txt))

