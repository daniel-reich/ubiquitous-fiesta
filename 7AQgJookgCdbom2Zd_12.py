
import re
def pig_latin(txt):
  a = txt.lower().split()
  empty = []
  vowels = ['a','e','i','o','u','A','E','I','O','U']
  for i in a:
    if i[0] in vowels:
      empty.append(i + 'way')
    else:
      empty.append(i[1:] + i[0] + 'ay')
  b = ' '.join(empty)
  b = re.sub(r'[^\w\s]','',b)
  return b[0].upper() + b[1:] + txt[-1]

