
vows = 'aeiou'
cons = 'bcdfghjklmnpqrstvwxyz'
​
def consonants(word):
  c = 0
  for i in word:
    if i.lower() in cons:
      c += 1
  return c
​
def vowels(word):
  v = 0
  for j in word:
    if j.lower() in vows:
      v += 1
  return v

