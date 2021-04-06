
import re
def consonants(word):
  word = re.sub("[^a-zA-Z]", "", word)
  word = re.sub("[aeiouAEIOU]", "", word)
  return len(word)
​
def vowels(word):
  word = re.sub("[^a-zA-Z]", "", word)
  word = re.sub("[^aeiouAEIOU]","",word)
  return len(word)

