
from re import sub
def dakiti(s):
  lst = sorted(s.split(), key=lambda x: sub(r'[a-z]', '', x))
  return ' '.join([sub(r'\d', '', i) for i in lst])

