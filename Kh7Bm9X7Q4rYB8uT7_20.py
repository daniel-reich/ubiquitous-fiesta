
def is_vowel_sandwich(s):
  if len(s)-3:
    return False
  return s[0] not in "aeiou" and s[1] in "aeiou" and s[2] not in "aeiou"

