
def consonants(word):
  return sum([1 for c in word.lower() if c.isalpha() and c not in ['a', 'e', 'i', 'o', 'u']])
​
def vowels(word):
  return sum([1 for c in word.lower() if c.isalpha() and c in ['a', 'e', 'i', 'o', 'u']])

