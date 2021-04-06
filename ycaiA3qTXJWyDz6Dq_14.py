
def consonants(word):
  return len([x for x in word if x.lower() in 'bcdfghjklmnpqrstvwxyz'])
​
def vowels(word):
  return len([x for x in word if x.lower() in 'aeiou'])

