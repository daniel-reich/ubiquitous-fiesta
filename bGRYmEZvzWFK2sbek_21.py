
def get_missing_letters(s):
  a = ''
  for i in range(97,123):
    if chr(i) not in s:
      a += chr(i)
  return a

