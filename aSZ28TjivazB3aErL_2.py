
def letters_only(s):
  return s == s.lower() and s.replace(' ', '').isalpha()

