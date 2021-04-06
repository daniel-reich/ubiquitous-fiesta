
def is_vowel_sandwich(s):
  con = lambda x: x not in 'aeiou'
  return len(s) == 3 and con(s[0]) and not con(s[1]) and con(s[2])

