
import re
​
​
def translate_word(word):
  if len(word) == 0:
    return ''
  word_indexes = [(m.start(0), m.end(0)) for m in re.finditer('[a-zA-Z]', word)]
  translatable_word = word[min(word_indexes)[0] : max(word_indexes)[1]]
  is_capitalized = translatable_word[0].isupper()
  translatable_word = translatable_word.lower().lstrip().rstrip()
  index = get_index(translatable_word)
  if index == 0:
    translatable_word = translatable_word + 'yay'
  else:
    translatable_word = translatable_word[index:] + translatable_word[:index] + 'ay' 
  
  if is_capitalized:
    translatable_word = translatable_word.capitalize()
  return word.replace(word[min(word_indexes)[0] : max(word_indexes)[1]], translatable_word)
​
def translate_sentence(sentence):
  str = []
  for index,word in enumerate(sentence.split()):
    str.append(translate_word(word))
  return " ".join(str)
​
def get_index(word):
  for index,value in enumerate(word):
    if value.lower() in 'aeiou':
      return index
      break

