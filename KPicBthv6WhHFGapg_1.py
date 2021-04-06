
def count_syllables(txt):
  return sum(1 for i in txt.lower() if i in 'aeiou')

