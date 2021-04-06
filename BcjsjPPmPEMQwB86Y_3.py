
def get_vowel_substrings(txt):
  vowels = ["a", "e", "i", "o", "u"]
  result = []
  for letter in range(len(txt)):
    if txt[letter] in vowels:
      for letter2 in range(letter, len(txt)):
        if txt[letter2] in vowels:
          res = txt[letter : letter2 + 1]
          if res not in result:
            result.append(res)
  return sorted(result)
​
def get_consonant_substrings(txt):
  vowels = ["a", "e", "i", "o", "u"]
  result = []
  for letter in range(len(txt)):
    if txt[letter] not in vowels:
      for letter2 in range(letter, len(txt)):
        if txt[letter2] not in vowels:
          res = txt[letter : letter2 + 1]
          if res not in result:
            result.append(res)
  return sorted(result)

