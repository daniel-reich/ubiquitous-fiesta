
def add_letters(a):
  if not sum([ord(i) - 96 for i in a]) % 26:
    return 'z'
  else:
    return chr(sum([ord(i) - 96 for i in a]) % 26 + 96)

