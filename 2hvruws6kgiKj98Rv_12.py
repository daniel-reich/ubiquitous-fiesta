
def to_scottish_screaming(txt):
  import re
  return re.sub('[aeiouAEIOU]', 'e', txt).upper()

