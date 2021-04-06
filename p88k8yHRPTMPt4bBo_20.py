
def count_vowels(txt):
  vo = 'aeiou'
  return len(list(filter(lambda x: x in vo, txt)))

