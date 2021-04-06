
def get_missing_letters(s):
  return ''.join(el for el in [chr(c) for c in range(97, 123) if chr(c) not in sorted(list(el for el in s))])

