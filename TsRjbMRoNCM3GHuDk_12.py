
import re
​
def syllabification(word):
  syll = re.findall(r'.[Aaeiou]', word)
  result = ''
  for s in syll[1:]:
    i = word.find(s)
    result += word[:i] + '.'
    word = word[i:]
    
  return result + word

