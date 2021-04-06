
def common_last_vowel(txt):
  return [i for i in txt.lower()[::-1] if i in 'aieou'][0]

