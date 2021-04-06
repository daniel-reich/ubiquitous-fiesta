
from itertools import combinations
​
def get_vowel_substrings(txt):
  res = [i for i in txt if i in 'aeiou']
  positions = [idx for idx, i in enumerate(txt) if i in 'aeiou']
  
  for a, b in combinations(positions, 2):
    if txt[b] in 'aeiou':
      res.append(txt[a: b+1])
  return sorted(set(res)) 
​
def get_consonant_substrings(txt):
  res = [i for i in txt if i not in 'aeiou']
  positions = [idx for idx, i in enumerate(txt) if i not in 'aeiou']
  
  for a, b in combinations(positions, 2):
    if txt[b] not in 'aeiou':
      res.append(txt[a: b+1])
  return sorted(set(res))

