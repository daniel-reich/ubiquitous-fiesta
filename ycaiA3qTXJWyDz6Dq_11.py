
def consonants(word):
  return sum(word.lower().count(c) for c in 'bcdfghjklmnpqrstvwxyz')
  
def vowels(word):
  return sum(word.lower().count(v) for v in 'aeiou')

