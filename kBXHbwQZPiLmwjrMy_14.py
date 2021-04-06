
import re
from string import ascii_uppercase
​
def translate_word(word):
  if word == "":
    return word
  upper = False
  if re.search(r"\b(\w)", word).group(1) in ascii_uppercase:
    upper = True
    word = word.lower()
​
  rv = ""
  if re.search(r"\b([aeiou])+.*", word) is not None:
    rv = re.sub(
      r"(\W*)([aeiou]+)(\w*)(\W*)",
      r"\1\2\3yay\4",
      word
      )
  else:
    rv = re.sub(
      r"(\W*)([^aeiou]+)([aeiou]+\w*)(.*)",
      r"\1\3\2ay\4",
      word
      )
  
  if upper:
    for i, c in enumerate(rv):
      if c.isalpha():
        break
    return rv[:i] + rv[i:].capitalize() 
  else:
    return rv
​
def translate_sentence(sentence):
  if len(sentence) < 1:
    return sentence
  new_sentence = ""
  for word in sentence.split(" "):
    new_sentence += translate_word(word) + " "
    
  return new_sentence.strip()

