
import re
def pig_latin_sentence(sentence):
  res = []
  for word in sentence.split():
    vp = re.search('[aeiou]', word).start()
    if vp:
      res.append(word[vp:] + word[:vp] + 'ay')
    else:
      res.append(word + 'way')
  return ' '.join(res)

