
import re
​
def pig_latin_sentence(txt):
  lst = []
  for w in txt.split():
    onset, coda = re.findall('([^aeiou]*)(\w+)', w)[0]
    lst += ['{}{}{}ay'.format(coda, onset, 'w' * (not onset))]
  return ' '.join(lst)

