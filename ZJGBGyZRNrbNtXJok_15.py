
def nearest_vowel(s):
  vowels = 'aeiou'
  lower = ord(s) - 1
  higher = ord(s) + 1
  if s in vowels:
    return s
  while chr(lower) not in vowels and chr(higher) not in vowels:
    lower -= 1
    higher += 1
  if chr(lower) in vowels:
    return chr(lower)
  return chr(higher)

