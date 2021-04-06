
def consonants(word):
  return sum(1 for i in word.lower() if i in "bcdfghjklmnpqrstvwxyz")
​
def vowels(word):
  return sum(1 for i in word.lower() if i in "aeiou")

