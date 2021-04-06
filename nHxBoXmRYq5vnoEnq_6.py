
def vowels(s):
  if not s: return 0
  return (1 if s[0] in 'aeiouAEIOU' else 0) + vowels(s[1:])

