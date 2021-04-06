
import re
def first_place(r):
  return ''.join(filter(str.isalnum, r))[-1]  if re.search('[a-zA-Z]+', r) else None

