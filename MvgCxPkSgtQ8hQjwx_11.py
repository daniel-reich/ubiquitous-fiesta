
def remove_vowels(txt):
  return txt.translate({ord(c):'' for c in "AEOUIaeoiu"})

