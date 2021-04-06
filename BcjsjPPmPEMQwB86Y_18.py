
vowels = ['a', 'e', 'i', 'o', 'u']
def get_vowel_substrings(txt):
  global vowels
  return sorted(set([txt[i: j + 1] for j in range(len(txt)) for i in range(j + 1) if txt[i] in vowels
      if txt[j] in vowels]))
​
def get_consonant_substrings(txt):
  global vowels
  return sorted(set([txt[i: j + 1] for j in range(len(txt)) for i in range(j + 1) if txt[i] not in vowels if txt[j]
      not in vowels]))

