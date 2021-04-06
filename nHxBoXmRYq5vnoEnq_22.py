
def vowels(s):
  if not s:
    return 0
  else:
    return (1 if s[0] in 'aeiou' else 0) + vowels(s[1:])

