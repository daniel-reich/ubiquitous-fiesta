
import re
​
def translate_word(word: str):
  vowels = re.findall(r'[aeuioAEUIO]', word)
  try:
    idx = word.index(vowels[0])
    if idx > 0:
      ret_word = word[idx:] + word[:idx] + 'ay'
    else:
      ret_word = word + 'yay'
​
  except IndexError:
    return ''
​
  if word[0].isupper():
    return (ret_word.lower()).capitalize()
  else:
    return ret_word
​
​
​
​
def translate_sentence(sentence):
  words = sentence.split()
​
  punctuation_before = [re.findall(r'([^\w]+)[\w]', word) for word in words]
  punctuation_after = [re.findall(r'[\w]([^\w]+)', word) for word in words]
​
  words = [re.sub(r'[:.,"?!\'/_\\()<>{}\[\];-]*(\w+)[:.,"?!\'/_\\()<>{}\[\];-]*', r'\1', word) for word in words]
  words = [translate_word(word) for word in words]
​
  ret_words = []
​
  for word, punct_before, punct_after in zip(words, punctuation_before, punctuation_after):
    if punct_after and punct_before:
      ret_words.append(punct_before[0] + word + punct_after[0])
​
    elif punct_before:
      ret_words.append(punct_before[0] + word)
​
    elif punct_after:
      ret_words.append(word + punct_after[0])
​
    else:
      ret_words.append(word)
​
  return ' '.join(ret_words)

