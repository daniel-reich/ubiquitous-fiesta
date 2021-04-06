
def consonants(word):
  return sum(c.isalpha() and c not in "aeiou" for c in word.lower())
​
def vowels(word):
  return sum(c.lower() in "aeiou" for c in word)

