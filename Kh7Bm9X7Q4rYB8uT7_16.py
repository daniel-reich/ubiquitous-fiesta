
def is_vowel_sandwich(s):
  return s[0] not in "aeiou" and s[2] not in "aeiou" and s[1] in "aeiou" if len(s)==3 else False

