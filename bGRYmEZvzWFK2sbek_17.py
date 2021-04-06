
def get_missing_letters(s):
  return ''.join([chr(i+96) for i in range(1,27) if chr(i+96) not in s])

