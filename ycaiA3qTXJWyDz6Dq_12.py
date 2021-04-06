
def consonants(word):
  count = 0
  consonant_list = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
  for i in word.lower():
    if i in consonant_list:
      count += 1
  return count
  
def vowels(word):
  count = 0
  vowel_list = ["a", "e", "i", "o", "u"]
  for i in word.lower():
    if i in vowel_list:
      count += 1
  return count

