
def consonants(word):
  vol="aouie"
  return len([c for c in word.lower() if c not in vol and c.isalpha()])
​
def vowels(word):
  vol="aouie"
  return len([c for c in word.lower() if c in vol and c.isalpha()])

