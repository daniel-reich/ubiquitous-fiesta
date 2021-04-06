
import re
def syllabification(word):
  new_word = ""
  syllable = re.compile(r'[^Aaeiou][Aaeiou][^Aaeiou]*$|[^Aaeiou][Aaeiou](?=[^Aaeiou][Aaeiou])|[^Aaeiou][Aaeiou][^Aaeiou](?=[^Aaeiou])')
  while True:
    if word == syllable.match(word).group(0):
      return new_word + word
    new_word += syllable.match(word).group(0) + "."
    word = word[len(syllable.match(word).group(0))::]

