
def vow_replace(txt, vowel):
  return "".join(vowel if i in 'aeiou' else i for i in txt)

