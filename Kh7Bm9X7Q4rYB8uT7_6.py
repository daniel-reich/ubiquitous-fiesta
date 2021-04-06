
def is_vowel_sandwich(s):
  if s[0] not in 'aeiou' and s[-1] not in 'aeiou' and len(s) > 2:
    if s[1:-1] in 'aeiou':
      return True
  return False

