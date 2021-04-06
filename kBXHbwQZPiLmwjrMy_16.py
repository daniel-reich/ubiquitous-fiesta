
import re
from string import punctuation
​
def translate_word(word):
    list_word = list(word)
    if list_word == []: return ''
    letters = [char.lower() for char in list_word if char not in punctuation]
    if letters[0] not in 'aeiouAEIOU':
        while letters[0] not in 'aeiouAEIOU':
            letters.append(letters.pop(0))
        letters.append('ay')
    else: letters.append('yay')
    for count,char in enumerate(list_word):
        if char in punctuation and count == 0:
            letters.insert(0,char)
        elif char in punctuation:
            letters.append(char)
    for index in [list_word.index(x) for x in list_word if x.isupper()]:
        letters[index] = letters[index].upper()
    return ''.join(letters)
​
def translate_sentence(sentence):
  return ' '.join([translate_word(word) for word in sentence.split()])

