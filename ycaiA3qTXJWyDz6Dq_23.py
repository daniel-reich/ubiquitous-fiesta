
from string import ascii_letters
def consonants(word):
  return sum([1 for i in word.lower() if i not in 'aeuio' and i in ascii_letters])
def vowels(word):
  return sum([1 for i in word.lower() if i in 'aeuio' and i in ascii_letters])

