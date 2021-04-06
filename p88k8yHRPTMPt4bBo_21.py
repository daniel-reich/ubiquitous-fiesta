
# Don't redefine each run (or loop!).
vowels = ('a', 'e', 'i', 'o', 'u')
​
def count_vowels(txt):
  vowel_n = 0
  for chara in txt:
    if chara in vowels:
      vowel_n += 1
  return vowel_n

