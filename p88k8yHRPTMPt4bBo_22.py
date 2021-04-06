
def count_vowels(txt):
  return sum(txt.count(x) for x in 'a e i o u'.split())

