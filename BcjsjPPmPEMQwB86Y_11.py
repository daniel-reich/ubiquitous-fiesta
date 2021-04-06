
vowels = ["a","e","i","o","u"]
​
def get_vowel_substrings(txt):
  substrings = []
  for i in range(len(txt)):
    for j in range(len(txt)):
      if j<i: 
        continue
      elif txt[i] in vowels and txt[j] in vowels:
        if txt[i:j+1] not in substrings:
          substrings.append(txt[i:j+1])
  return sorted(substrings)
​
def get_consonant_substrings(txt):
  substrings = []
  for i in range(len(txt)):
    for j in range(len(txt)):
      if j<i: 
        continue
      elif txt[i] not in vowels and txt[j] not in vowels:
        if txt[i:j+1] not in substrings:
          substrings.append(txt[i:j+1])
  return sorted(substrings)

