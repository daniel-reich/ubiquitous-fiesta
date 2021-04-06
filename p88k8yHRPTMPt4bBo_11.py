
def count_vowels(txt):
  vowels = "aeiou"
  num_vow = 0
  for i in txt:
    if i in vowels:
      num_vow += 1
  return num_vow

