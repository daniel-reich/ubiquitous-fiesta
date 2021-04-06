
def consonants(word):
  return len([c for c in word.lower() if c in "bcdfghjklmnpqrstvwxyz"])
​
def vowels(word):
  return len([c for c in word.lower() if c in "aeiou"])

