
import re
​
def syllabification(word):
  C, V = '[^aeiouA]', '[aeiouA]'
  return '.'.join(re.findall('{}{}{}*(?=$|{})'.format(C,V,C,C), word))

