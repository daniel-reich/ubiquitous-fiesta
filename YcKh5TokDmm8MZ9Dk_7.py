
import re
def word(x):
  return re.sub(r'[^a-zA-Z]+','',x).lower()
def hidden_anagram(text, phrase):
  text,phrase = word(text),word(phrase)
  for i in range(0,len(text)-len(phrase)+1):
    if all(text[i:len(phrase)+i].count(x) == phrase.count(x) for x in set(phrase)):
      return text[i:len(phrase)+i]
  return 'noutfond'

