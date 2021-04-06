
import re
​
def hidden_anagram(text, phrase):
  phrase = re.sub(r'[^a-zA-Z]', '', phrase.lower())
  text = re.sub(r'[^a-zA-Z]', '', text.lower())
  for i in range(len(text)):
    if sorted(text[i:i+len(phrase)]) == sorted(phrase):
      return text[i:i+len(phrase)]
  return 'noutfond'

