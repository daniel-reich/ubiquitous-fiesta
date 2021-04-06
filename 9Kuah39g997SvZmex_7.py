
def common_last_vowel(txt):
  vowels = []
  for w in txt.lower().split():
    vowels.append([c for c in w if c in 'aeiou'][-1])
  return sorted(vowels, key=lambda v: vowels.count(v))[-1]

