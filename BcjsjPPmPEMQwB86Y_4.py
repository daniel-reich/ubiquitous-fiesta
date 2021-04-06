
def get_all(txt):
  s = [txt[a:b+1] for a in range(len(txt)) for b in range(len(txt)) if txt[a:b+1] != '']
  return sorted(list(set(s)))
​
def get_vowel_substrings(txt):
  return [s for s in get_all(txt) if s[0] in 'aeiou' and s[-1] in 'aeiou']
​
def get_consonant_substrings(txt):
  return [s for s in get_all(txt) if s[0] not in 'aeiou' and s[-1] not in 'aeiou']

