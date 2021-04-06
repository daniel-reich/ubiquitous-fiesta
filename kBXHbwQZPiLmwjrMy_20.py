
import re
​
def translate_word(word):
  if not word: return ''
    
  p1, onset, coda, p2 = re.findall('(\W*)([^aeiouAEIOU]*)(\w+)(\W*)', word)[0]
  up = (onset + coda)[0].isupper()
  
  res = '{}{}{}ay'.format(coda, onset, 'y' * (not onset)).lower()
  res = res.capitalize() if up else res
  
  return '{}{}{}'.format(p1, res, p2)
​
def translate_sentence(sentence):
  return ' '.join(translate_word(w) for w in sentence.split())

