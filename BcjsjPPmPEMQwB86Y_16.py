
def get_vowel_substrings(txt):
  vowels = 'aeiou'
  res = set()
  for start in range(len(txt)):
    for end in range(start+1,len(txt)+1):
      if txt[start:end][0] in vowels and txt[start:end][-1] in vowels:
        res.add(txt[start:end])
  return sorted([r for r in res])
​
def get_consonant_substrings(txt):
  vowels = 'aeiou'
  res = set()
  for start in range(len(txt)):
    for end in range(start+1,len(txt)+1):
      if txt[start:end][0] not in vowels and txt[start:end][-1] not in vowels:
        res.add(txt[start:end])
  return sorted([r for r in res])

