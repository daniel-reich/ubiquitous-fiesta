
import re
def x_pronounce(sentence):
  return ' '.join(word.replace('x', 'z') if bool(re.match('^x\S', word)) else 'ecks' if bool(re.match('^x$', word)) else word.replace('x', 'cks') for word in sentence.split())

