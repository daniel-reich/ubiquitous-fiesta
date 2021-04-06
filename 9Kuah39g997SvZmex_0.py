
def common_last_vowel(txt):
  return sorted(txt.lower(), key=lambda x: x in 'aeiou')[-1]

