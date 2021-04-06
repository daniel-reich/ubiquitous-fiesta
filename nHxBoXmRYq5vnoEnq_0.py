
def vowels(s):
  return 0 if not s else (s[0] in 'aeiou') + vowels(s[1:])

