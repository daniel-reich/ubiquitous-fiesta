
import re
def sigilize(d):
  d = d.upper()
  d = re.sub('[AEIOU ]', '', d)
  return ''.join([d[i] for i in range(len(d)) if d[i] not in d[i+1:]])

