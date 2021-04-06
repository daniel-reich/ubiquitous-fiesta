
def get_missing_letters(s):
  return ''.join(chr(i) for i in range(97, 123) if chr(i) not in s)

