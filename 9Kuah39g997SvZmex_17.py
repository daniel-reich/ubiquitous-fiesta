
def common_last_vowel(txt):
  return ' '.join([i for i in txt.lower() if i in 'aeiou'][-1])

