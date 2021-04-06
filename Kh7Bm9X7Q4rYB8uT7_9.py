
def is_vowel_sandwich(s):
  return len(s)==3 and s[1] in 'aeiou'and s[0] not in 'aeiou' and s[2] not in 'aeiou'

