
def vow_replace(word, vowel):
  return ''.join([i.replace(i,vowel) if i in 'aeiou' else i for i in word ])

