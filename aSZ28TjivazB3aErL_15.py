
def letters_only(s):
  return s == ''.join([i.lower() for i in s if i.isalpha() or i == ' ']) and len(s) > 0

