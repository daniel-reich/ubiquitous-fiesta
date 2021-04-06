
def is_vowel_sandwich(s):
  return [0, 1, 0] == [1 if l in 'aeiou' else 0 for l in s]

