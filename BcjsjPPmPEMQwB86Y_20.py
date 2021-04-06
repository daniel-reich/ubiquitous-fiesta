
def get_vowel_substrings(txt):
  vowels = "aeiou"
  lst = []
  str = ""
  for i in range(len(txt)):
    str = txt[i]
    if txt[i] in vowels:
      lst.append(txt[i])
      for j in txt[i+1:]:
        str += j
        if j in vowels:
          lst.append(str)
  return sorted(set(lst))
​
def get_consonant_substrings(txt):
  consonants = "bcdfghjklmnpqrstvwxyz"
  lst = []
  str = ""
  for i in range(len(txt)):
    str = txt[i]
    if txt[i] in consonants:
      lst.append(txt[i])
      for j in txt[i+1:]:
        str += j
        if j in consonants:
          lst.append(str)
  return sorted(set(lst))

