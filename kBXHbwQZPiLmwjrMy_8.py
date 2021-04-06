
import re
def translate_word(word):
  if (word == ""):
    return word
  vowel = False
  if (re.match("^[aeiouAEIOU]", word)):
    vowel = True
  if (vowel):
    return word+"yay"
  consonant = re.search("^[^aeiouAEIOU]+", word).group()
  clen = len(consonant)
  new_word = word[clen:]
  if (consonant[0].isupper()):
    new_word = list(new_word)
    new_word[0] = new_word[0].upper()
    new_word = "".join(new_word)
  consonant = consonant.lower()
  new_word += consonant+"ay"
  return new_word
​
def translate_sentence(sent):
  if (sent == ""):
    return sent
  sent += " "
  word_pat = r"\w+"
  not_word_pat = r"\W+"
  words = re.findall(word_pat, sent)
  not_words = re.findall(not_word_pat, sent)
  for i, c in enumerate(words):
    words[i] = translate_word(c)
  return "".join([words[i]+not_words[i] for i, c in enumerate(words)]).rstrip()

